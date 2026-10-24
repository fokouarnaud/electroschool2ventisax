Other principles detect further away, or detect objects that inductive sensors cannot see.

## Photoelectric sensors

A transmitter sends a beam of light (often infrared); a receiver detects its presence or absence. Three arrangements:

![Three photoelectric arrangements: through-beam with separate transmitter and receiver, retro-reflective with a reflector, diffuse with the object returning the light](/static/content/moteurs/en/m4/photo.svg)

- **through-beam**: transmitter and receiver face each other; the object breaks the beam. The longest range, up to tens of metres.
- **retro-reflective**: transmitter and receiver in the same housing, facing a **reflector**; the object breaks the beam on its way out and back.
- **diffuse** (proximity): the object itself returns the light; shorter range, which depends on the object's colour.

## Hall-effect sensors

A **Hall-effect** sensor detects a **magnetic field**: a magnet fixed to the moving part makes it switch. It is found on cylinders (piston position), in brushless motors and in speed sensors.

## Ultrasonic sensors

The sensor emits a burst of ultrasound and measures the **time** the echo takes to return. Sound travels out and back at about 340 m/s in air: the distance is **d = v × t / 2**.

![Ultrasonic sensor: the wave travels to the object and back; the distance is v × t / 2](/static/content/moteurs/en/m4/ultrasons.svg)

**Example.** The echo returns after 5 ms: d = 340 × 0.005 / 2 = **0.85 m**. Ultrasound detects transparent objects, liquids and bulk materials, whatever their colour: it is used to measure the level in a tank.

## Key points

- Through-beam, retro-reflective, diffuse: from longest to shortest range.
- Hall effect: detects a magnet.
- Ultrasound: d = v × t / 2, with v ≈ 340 m/s.
