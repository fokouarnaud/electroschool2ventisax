from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext as _

from courses.access import accessible_formations
from courses.models import Partie
from progress.models import Announcement
from progress.services import exam_unlocked, module_completed, progress_pct

from .models import SignupThrottle, User
from .signup import (
    SignupForm, client_ip_hash, create_pending_learner, email_verification_token, is_signup_throttled,
    send_verification_email,
)


@login_required
def dashboard(request):
    if request.user.is_trainer or (request.user.is_platform_admin and not request.user.enrollments.exists()):
        return redirect("trainer_table")
    parts = []
    formations = accessible_formations(request.user)
    for partie in Partie.objects.filter(formation__in=formations).order_by("formation__order", "formation", "order"):
        parts.append({
            "partie": partie,
            "progress": progress_pct(request.user, partie),
            "modules": [{"module": m, "done": module_completed(request.user, m)} for m in partie.modules.all()],
            "exam_unlocked": exam_unlocked(request.user, partie),
        })
    announcements = Announcement.objects.filter(promotion__enrollments__user=request.user)[:5]
    return render(request, "accounts/dashboard.html", {"parts": parts, "announcements": announcements})


def signup(request):
    """Inscription publique (US-02, US-03)."""
    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_bot:  # piège rempli : on simule un succès sans rien créer
            return redirect("signup_done")
        ip_hash = client_ip_hash(request)
        if is_signup_throttled(ip_hash):
            return HttpResponse(_("Trop d'inscriptions depuis cette connexion. Réessayez dans une heure."), status=429)
        if form.is_valid():
            SignupThrottle.objects.create(ip_hash=ip_hash)
            user = create_pending_learner(form)
            send_verification_email(request, user)
            return redirect("signup_done")
    return render(request, "accounts/signup.html", {"form": form})


def signup_done(request):
    return render(request, "accounts/signup_done.html")


def verify_email(request, uidb64, token):
    try:
        user = User.objects.get(pk=force_str(urlsafe_base64_decode(uidb64)))
    except (User.DoesNotExist, ValueError, TypeError, OverflowError):
        user = None
    if user is None or not email_verification_token.check_token(user, token):
        return HttpResponseBadRequest(_("Ce lien de confirmation est invalide ou a déjà servi."))
    user.is_active = True
    user.email_verified = True
    user.save(update_fields=["is_active", "email_verified"])
    messages.success(request, _("Adresse confirmée. Vous pouvez vous connecter."))
    return redirect("login")
