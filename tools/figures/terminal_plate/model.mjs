// Modèle de la plaque à bornes d'un moteur triphasé (moteurs, M2, section 02-reperage) : seule source des repères, des barrettes et des tensions de la figure.
export const TOP = ["U1", "V1", "W1"];
// Sorties décalées d'un cran : sous chaque entrée, la sortie de l'enroulement précédent.
export const BOTTOM = TOP.map((_, c) => `${TOP[(c + 2) % 3][0]}2`);
// Colonne et rangée d'une borne (rangée 0 au fond, 1 devant).
export const place = (mark) => (mark[1] === "1" ? [TOP.indexOf(mark), 0] : [BOTTOM.indexOf(mark), 1]);
export const winding = (letter) => [`${letter}1`, `${letter}2`];
// Étoile : une barrette sur la rangée des sorties ; triangle : une barrette verticale par colonne.
export const links = (coupling) => (coupling === "star" ? [BOTTOM.slice()] : TOP.map((m, c) => [m, BOTTOM[c]]));
// Réseau qui convient à un moteur 230/400 V dans chaque couplage (tension entre phases, en V).
export const NETWORK = { star: 400, delta: 230 };
// Étoile : tension simple U / √3 ; triangle : tension composée U.
export const windingVoltage = (coupling, network) => (coupling === "star" ? network / Math.sqrt(3) : network);
export const LIFT = 10; // hauteur dont les barrettes se lèvent pendant le changement (unités du dessin)
export const SWAP_S = 0.8; // s affichées pour changer les barrettes (mouvement illustratif)
