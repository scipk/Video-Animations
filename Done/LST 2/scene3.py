from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class ExerciseProblem(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(str="en", tld="com", transcription_model='base'))

        text1 = Tex("Block Diagram", " $\\rightarrow$ ", "System Equations")
        text2 = Tex("System Equations", " $\\rightarrow$ ", "Block Diagram")
        text3 = Text("System Decomposition")

        with self.voiceover("It is very useful to represent a complex system as an interconnection of simple blocks. <bookmark mark='A'/>We call that System Decomposition.") as tracker:
            self.play(FadeIn(text1))
            self.wait(1)
            self.play(TransformMatchingTex(text1, text2))
            self.wait_until_bookmark("A")
            self.play(FadeOut(text2), FadeIn(text3))

        with self.voiceover("Here's an exercise problem.") as tracker:
            self.play(FadeOut(text3), run_time=tracker.duration)

        exercise_text_1 = Tex("""EXERCISE: Consider a system $P_2$ that\n
                            maps each input $u$ to the solutions $y$ of:""", font_size=30).to_edge(UP)
        exercise_eq_1_1 = MathTex(r"\begin{bmatrix}\dot{x}_1\\\dot{x}_2\end{bmatrix}=", r"\begin{bmatrix}2 & 0 \\ -2 & 1\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}", r"+", r"\begin{bmatrix}3\\2\end{bmatrix}u").next_to(exercise_text_1, DOWN, buff=0.5)
        exercise_eq_2_1 = MathTex(r"y=", r"\begin{bmatrix}2 & 4\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}").next_to(exercise_eq_1_1, DOWN, buff=0.5)
        exercise_text_2 = Tex("""Represent this system in terms of a block diagram consisting only of:\n
                                - Integrator Systems\n
                                - Summation Blocks\n
                                - Gain Memoryless Systems""", font_size=30).next_to(exercise_eq_2_1, DOWN, buff=0.5)

        with self.voiceover("Consider a system P2 that maps each input U to the solutions Y <bookmark mark='A'/> of the following equations.") as tracker:
            self.play(Create(exercise_text_1), run_time=tracker.time_until_bookmark("A"))
            self.play(Create(exercise_eq_1_1), Create(exercise_eq_2_1))
            self.wait(1)

        with self.voiceover("We're then told to represent the system in terms of block diagrams consisting of only these types.") as tracker:
            self.play(Create(exercise_text_2))

        with self.voiceover("First, we'll begin by deriving our equations.") as tracker:
            self.play(
                FadeOut(exercise_text_1, exercise_text_2),
                exercise_eq_2_1.animate.to_corner(UL),
                exercise_eq_1_1.animate.move_to(ORIGIN),
                run_time=tracker.duration
            )

        exercise_eq_1_2 = MathTex(r"\begin{bmatrix}\dot{x}_1\\\dot{x}_2\end{bmatrix}=", r"\begin{bmatrix}2x_1 + 0x_2 \\ -2x_1 + 1x_2\end{bmatrix}", r"+", r"\begin{bmatrix}3u\\2u\end{bmatrix}")
        exercise_eq_1_3 = MathTex(r"\begin{bmatrix}\dot{x}_1\\\dot{x}_2\end{bmatrix}=", r"\begin{bmatrix}2x_1+0x_2+3u\\-2x_1+1x_2+2u\end{bmatrix}")

        with self.voiceover("The state equation can be turned into this.") as tracker:
            self.play(TransformMatchingTex(exercise_eq_1_1, exercise_eq_1_2))
            self.play(TransformMatchingTex(exercise_eq_1_2, exercise_eq_1_3))
            
        state_eq_1 = MathTex(r"\dot{x}_1=2x_1+3u").move_to(UP)
        state_eq_2 = MathTex(r"\dot{x}_2=-2x_1+1x_2+2u").move_to(DOWN)
        state_equations = VGroup(state_eq_1, state_eq_2)
        
        with self.voiceover("Which simply gives us these two equations.") as tracker:
            self.play(FadeOut(exercise_eq_1_3), FadeIn(state_equations))
        
        output_equation = MathTex(r"y=", r"2x_1+4x_2")

        with self.voiceover("and the output equation can be turned into this.") as tracker:
            self.play(
                state_equations.animate.scale(0.8).to_corner(UL),
                exercise_eq_2_1.animate.move_to(ORIGIN)
            )
            self.play(TransformMatchingTex(exercise_eq_2_1, output_equation))
        
        with self.voiceover("Now that we're done finding these three equations <bookmark mark='A'/> we can go to Simulink.") as tracker:
            self.play(
                state_eq_1.animate.scale(1.25).move_to(UP),
                state_eq_2.animate.scale(1.25).move_to(ORIGIN),
                output_equation.animate.move_to(DOWN),
                run_time=tracker.time_until_bookmark("A")
            )