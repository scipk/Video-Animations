from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class StateSpaceSystems(VoiceoverScene):
    def construct(self):
        # Set the text-to-speech service
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # --- INTRO ---
        title = Tex("State-Space Linear Systems").scale(1.2).to_edge(UP)
        eq_labels = Tex("1. The State Equation\\\\2. The Output Equation").next_to(title, DOWN, buff=0.5)

        with self.voiceover(text="State-space linear systems have two equations: The State Equation and the Output Equation.") as tracker:
            self.play(Write(title))
            self.play(FadeIn(eq_labels))

        with self.voiceover(text="In Continuous-Time, they look like this:") as tracker:
            continuous_title = Tex("Continuous-Time").to_edge(UP)
            self.play(
                Transform(title, continuous_title),
                FadeOut(eq_labels)
            )

        # --- CONTINUOUS TIME EQUATIONS ---
        state_eq = MathTex(r"\dot{x}(t) = A(t)x(t) + B(t)u(t)")
        output_eq = MathTex(r"y(t) = C(t)x(t) + D(t)u(t)")
        
        eq_group = VGroup(state_eq, output_eq).arrange(DOWN, buff=1.0)

        with self.voiceover(text="1. The state equation is an ordinary differential equation") as tracker:
            self.play(Write(state_eq))

        with self.voiceover(text="And the output equation is a nice and easy") as tracker:
            self.play(Write(output_eq))

        self.play(eq_group.animate.to_edge(LEFT).scale(0.8))

        # --- SYSTEM PARAMETERS ---
        param_title = Tex("System Parameters").to_edge(UP)
        
        # Using separate strings to easily isolate "(t)" for highlighting later
        param_A = MathTex(r"A", r"(t)", r" \text{ - state matrix}")
        param_B = MathTex(r"B", r"(t)", r" \text{ - input matrix}")
        param_C = MathTex(r"C", r"(t)", r" \text{ - output matrix}")
        param_D = MathTex(r"D", r"(t)", r" \text{ - feedthrough matrix}")
        
        params_group = VGroup(param_A, param_B, param_C, param_D).arrange(DOWN, aligned_edge=LEFT).next_to(eq_group, RIGHT, buff=1.5)

        with self.voiceover(text="These are called the system parameters.") as tracker:
            self.play(
                Transform(title, param_title),
                Write(params_group)
            )

        # --- LTV SYSTEM ---
        ltv_label = Tex("Linear Time-Variant System (LTV)").set_color(YELLOW).next_to(params_group, DOWN, buff=0.5)
        
        with self.voiceover(text="If system parameters rely on time we call the system a Linear Time-Variant System, or LTV for short.") as tracker:
            # Highlight the (t) in each parameter
            self.play(
                param_A[1].animate.set_color(YELLOW),
                param_B[1].animate.set_color(YELLOW),
                param_C[1].animate.set_color(YELLOW),
                param_D[1].animate.set_color(YELLOW),
            )
            self.play(FadeIn(ltv_label))

        # --- LTI SYSTEM ---
        lti_label = Tex("Linear Time-Invariant System (LTI)").set_color(GREEN).move_to(ltv_label)
        
        # New parameter strings without (t)
        param_A_lti = MathTex(r"A", r" \text{ - state matrix}")
        param_B_lti = MathTex(r"B", r" \text{ - input matrix}")
        param_C_lti = MathTex(r"C", r" \text{ - output matrix}")
        param_D_lti = MathTex(r"D", r" \text{ - feedthrough matrix}")
        
        params_group_lti = VGroup(param_A_lti, param_B_lti, param_C_lti, param_D_lti).arrange(DOWN, aligned_edge=LEFT).move_to(params_group, aligned_edge=LEFT)

        with self.voiceover(text="However, if system parameters don't rely on time we call the system a Linear Time-Invariant System, or LTI for short.") as tracker:
            self.play(
                Transform(ltv_label, lti_label),
                # Remove the (t) by transforming to the LTI group
                Transform(param_A, param_A_lti),
                Transform(param_B, param_B_lti),
                Transform(param_C, param_C_lti),
                Transform(param_D, param_D_lti),
            )
            self.wait(1)

        # Clear screen for discrete time
        self.play(FadeOut(eq_group, params_group, param_A, param_B, param_C, param_D, ltv_label, title))

        # --- DISCRETE TIME ---
        discrete_title = Tex("Discrete-Time").to_edge(UP)
        discrete_def = MathTex(r"t \in \mathbb{N} := \{0, 1, 2, \dots\}").next_to(discrete_title, DOWN)

        with self.voiceover(text="There is another type of time, called Discrete-Time. That's when you treat time as an element of the set of all natural numbers. This way, we don't have to worry about every infinitely small value between, for example, 0 and 1.") as tracker:
            self.play(Write(discrete_title))
            self.play(FadeIn(discrete_def))

        with self.voiceover(text="In Discrete-Time, the State-Space Linear System equations are a bit different:") as tracker:
            self.play(discrete_def.animate.scale(0.7).to_corner(UR))

        # --- DISCRETE EQUATIONS ---
        discrete_state = MathTex(r"x(t+1) = A(t)x(t) + B(t)u(t)")
        diff_eq_label = Tex("Difference Equation", font_size=32, color=ORANGE).next_to(discrete_state, DOWN)
        
        discrete_output = MathTex(r"y(t) = C(t)x(t) + D(t)u(t)")
        
        discrete_group = VGroup(discrete_state, diff_eq_label, discrete_output).arrange(DOWN, buff=0.8)

        with self.voiceover(text="1. The state equation is like so") as tracker:
            self.play(Write(discrete_state))

        with self.voiceover(text="notice how this isn't an ODE. It's a Difference Equation.") as tracker:
            self.play(FadeIn(diff_eq_label, shift=UP))

        with self.voiceover(text="2. The output equation is pretty much the same") as tracker:
            self.play(Write(discrete_output))

        self.wait(2)