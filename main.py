from kittentts import KittenTTS

kitten = KittenTTS("KittenML/kitten-tts-nano-0.1")
TEXT="Bluetooth device connected to Nokia5000."
for voice in kitten.available_voices:
    output_file = f"{voice}-output.wav"
    print(f"Generating for voice {voice} in {output_file}")
    kitten.generate_to_file(TEXT,f"{voice}-output.wav",voice=voice)