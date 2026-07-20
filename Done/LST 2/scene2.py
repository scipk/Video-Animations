from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GeneralInterconnection(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(str="en", tld="com", transcription_model='base'))
        
        system1 = MathTex(r"P_1: \dot{x_1}=A_1x_1+B_1u_1,\space y_1=C_1x_1 + D_1u_1").move_to(UP)
        system2 = MathTex(r"P_2: \dot{x_2}=A_2x_2+B_2u_2,\space y_2=C_2x_2 + D_2u_2").move_to(DOWN)

        general_system = VGroup(system1, system2)

        with self.voiceover("Let's consider the following general-case of two interconnected systems:") as tracker:
            self.play(Create(general_system))

        with self.voiceover("P1 as you can see, has its state equation and its output equation. <bookmark mark='A'/>And so does P2.") as tracker:
            self.play(system1.animate.set_color(GREEN))
            self.wait_until_bookmark("A")
            self.play(system2.animate.set_color(GREEN))

        with self.voiceover("When finding the state-space for an interconnection, we use this general procedure:") as tracker:
            self.play(general_system.animate.set_color(WHITE).scale(0.5).to_corner(UL))

        text1 = Text("1. Write the complete state equation and output equation using matrices.", font_size=30).move_to(UP)
        text2 = Text("2. Try to isolate x such that it looks like this:", font_size=30).move_to(DL)
        text2_latex = MathTex(r"x=\begin{bmatrix}x_1 \\ x_2 \\ \vdots \\ x_n\end{bmatrix}").next_to(text2, RIGHT, buff=0.5)

        with self.voiceover("First we write the complete state equation and output equation using matrices") as tracker:
            self.play(FadeIn(text1))

        with self.voiceover("Then we try to isolate the stacked, tall vector $x$ such that it looks like this:") as tracker:
            self.play(FadeIn(text2), FadeIn(text2_latex))

class ParallelVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(str="en", tld="com", transcription_model='base'))

        u_statement = MathTex(r"u = u_1 = u_2")
        y_statement = MathTex(r"y =", r"y_1", r"+", r"y_2")
        given_statement = VGroup(u_statement, y_statement)

        with self.voiceover("As you can see, the first input isn't changed before going into either systems <bookmark mark='A'/>so U equals both U1 and U2.") as tracker:
            self.wait_until_bookmark("A")
            self.play(Create(u_statement))
            self.play(u_statement.animate.to_corner(UL))

        with self.voiceover("But the final output is the combination of both systems' outputs <bookmark mark='A'/>so Y equals Y1 + Y2.") as tracker:
            self.wait_until_bookmark("A")
            self.play(Create(y_statement))
            self.play(y_statement.animate.next_to(u_statement, RIGHT, buff=1))

        state_equation_1 = MathTex(r"\dot{x} =", r"\begin{bmatrix} \dot{x_1} \\ \dot{x_2} \end{bmatrix}")

        with self.voiceover("Now that we're setup let's write the state equation.") as tracker:
            self.play(
                given_statement.animate.scale(0.8).to_corner(UL),
                Create(state_equation_1),
                run_time = tracker.duration
            )

        state_equation_2 = MathTex(r"\dot{x} =", r"\begin{bmatrix} A_1x_1+B_1u_1 \\ A_2x_2+B_2u_2 \end{bmatrix}")

        with self.voiceover("Each system has its own system equation.") as tracker:
            self.play(TransformMatchingTex(state_equation_1, state_equation_2))

        state_equation_3 = MathTex(r"\dot{x} =", r"\begin{bmatrix}A_1x_1 \\ A_2x_2\end{bmatrix}+\begin{bmatrix}B_1u_1 \\ B_2u_2\end{bmatrix}")

        with self.voiceover("By the matrix addition property we can split it up.") as tracker:
            self.play(TransformMatchingTex(state_equation_2, state_equation_3))

        state_equation_3_5 = MathTex(r"\dot{x} =", r"\begin{bmatrix}A_1x_1 \\ A_2x_2\end{bmatrix}+\begin{bmatrix}B_1u \\ B_2u\end{bmatrix}")

        with self.voiceover("Also, We know can just use U for U1 and U2.") as tracker:
            self.play(TransformMatchingTex(state_equation_3, state_equation_3_5), u_statement.animate.set_color(GREEN))

        state_equation = MathTex(r"\dot{x} =", r"\begin{bmatrix}A_1 & 0 \\ 0 & A_2\end{bmatrix}\begin{bmatrix}x_1 \\ x_2\end{bmatrix}+\begin{bmatrix}B_1 \\ B_2\end{bmatrix}u")
        
        with self.voiceover("And by block matrix multiplication and scalar multiplication over a vector, we get this.") as tracker:
            self.play(u_statement.animate.set_color(WHITE))
            self.play(TransformMatchingTex(state_equation_3_5, state_equation))

        with self.voiceover("Next, let's do that with the output equation.") as tracker:
            self.play(
                state_equation.animate.next_to(given_statement, DOWN, buff=0.3).scale(0.8),
                y_statement.animate.scale(1.25).move_to(ORIGIN)
            )

        output_equation_1 = MathTex(r"y =", r"(", r"C_1x_1", r"+", r"D_1u_1", r")", r"+", r"(", r"C_2x_2", r"+", r"D_2u_2", r")")

        with self.voiceover("Each system has its own output equation.") as tracker:
            self.play(TransformMatchingTex(y_statement, output_equation_1))
        
        output_equation_2 = MathTex(r"y =", r"(", r"C_1x_1", r"+", r"C_2x_2", r")", r"+", r"(", r"D_1u_1", r"+", r"D_2u_2", r")")

        with self.voiceover("We can rearrange our terms via addition."):
            self.play(TransformMatchingTex(output_equation_1, output_equation_2))

        output_equation_2_5 = MathTex(r"y =", r"(", r"C_1x_1", r"+", r"C_2x_2", r")", r"+", r"(", r"D_1u", r"+", r"D_2u", r")")

        with self.voiceover("We know can just use U for U1 and U2.") as tracker:
            self.play(TransformMatchingTex(output_equation_2, output_equation_2_5), u_statement.animate.set_color(GREEN))
        
        output_equation = MathTex(r"y =", r"\begin{bmatrix}C_1 & C_2\end{bmatrix}\begin{bmatrix}x_1 \\ x_2\end{bmatrix}+(D_1+D_2)u")

        with self.voiceover("By definition of Matrix Vector Multiplication and the Distributive Property, we get this.") as tracker:
            self.play(u_statement.animate.set_color(WHITE))
            self.play(TransformMatchingTex(output_equation_2_5, output_equation))

        with self.voiceover("And voila! Now you know how to derive the Parallel Interconnection equations.") as tracker:
            self.play(
                FadeOut(u_statement),
                output_equation.animate.move_to(DOWN),
                state_equation.animate.scale(1.25).move_to(UP)
            )