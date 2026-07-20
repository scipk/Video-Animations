from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Animation1(VoiceoverScene):
    def construct(self):
        # Initialize the Google TTS voiceover service
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # --- Object Definitions ---
        # A sleek, dark-filled box with a blue border
        box = Rectangle(width=3.5, height=2.2, color=BLUE, fill_color=BLACK, fill_opacity=1)
        
        # Center the text and question mark inside the box
        question_mark = Text("?", font_size=60, color=GRAY).move_to(box.get_center())
        box_text = Text("Black Box", font_size=28, color=WHITE).move_to(box.get_center())

        # Main input/output arrows (centered vertically at y=0)
        arrow_in = Arrow(start=LEFT * 4.5, end=LEFT * 1.8, color=WHITE)
        label_in = Text("In", font_size=24).next_to(arrow_in, UP, buff=0.1)
        
        arrow_out = Arrow(start=RIGHT * 1.8, end=RIGHT * 4.5, color=WHITE)
        label_out = Text("Out", font_size=24).next_to(arrow_out, UP, buff=0.1)

        # Create additional complex arrows for the "nightmare" phase
        y_offsets = [-0.8, -0.4, 0.4, 0.8]
        left_arrows = VGroup()
        right_arrows = VGroup()
        
        for y in y_offsets:
            arr_in = Arrow(start=LEFT * 4.5 + UP * y, end=LEFT * 1.8 + UP * y, color=RED, stroke_width=3)
            arr_out = Arrow(start=RIGHT * 1.8 + UP * y, end=RIGHT * 4.5 + UP * y, color=RED, stroke_width=3)
            left_arrows.add(arr_in)
            right_arrows.add(arr_out)


        # --- Animation Sequence ---

        # Segment 1: Introduction to the System
        with self.voiceover(
            text="With a system like that, you knew what went in and you saw what came out but you didn't know what's inside."
        ) as tracker:
            # Draw the system box
            self.play(Create(box), run_time=1.5)
            # Show the "In" arrow and label
            self.play(Create(arrow_in), Write(label_in), run_time=1.2)
            # Show the "Out" arrow and label
            self.play(Create(arrow_out), Write(label_out), run_time=1.2)
            # Fade in the mystery question mark inside the box
            self.play(FadeIn(question_mark), run_time=1.0)
            
        # Segment 2: Naming the "Black Box"
        with self.voiceover(text="That inside is called the 'Black Box'.") as tracker:
            # Swap the question mark for the text "Black Box"
            self.play(
                FadeOut(question_mark, shift=DOWN),
                Write(box_text),
                run_time=2.0
            )

        # Segment 3: The "Simple" Phase
        with self.voiceover(text="When you're doing something simple, it's not that bad.") as tracker:
            # Pulsing the arrows green to emphasize a smooth, simple flow
            self.play(
                arrow_in.animate.set_color(GREEN),
                arrow_out.animate.set_color(GREEN),
                run_time=2
            )
            self.play(
                arrow_in.animate.set_color(WHITE),
                arrow_out.animate.set_color(WHITE),
                run_time=1
            )

        # Segment 4: The Complexity / Nightmare Phase
        with self.voiceover(
            text="When things get as complex as rockets though, it becomes a nightmare."
        ) as tracker:
            # Rapidly spawn the extra red arrows to show high complexity (MIMO system)
            self.play(
                LaggedStart(*[Create(a) for a in left_arrows], lag_ratio=0.12),
                LaggedStart(*[Create(a) for a in right_arrows], lag_ratio=0.12),
                run_time=2.5
            )
            # Shake the box and turn everything red to emphasize "nightmare"
            self.play(
                box.animate.set_color(RED),
                box_text.animate.set_color(RED),
                ApplyWave(box),
                ApplyWave(box_text),
                run_time=2.0
            )
            self.wait(1) # Final pause before ending