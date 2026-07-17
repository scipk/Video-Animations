from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService

# Vertical Video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_height = 14.22
config.frame_width = 8

class LST1Short(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com", transcription_model='base'))
        # self.set_speech_service(RecorderService())

        text = Text("State-Space Linear Systems", font_size=40)

        with self.voiceover(text="What are State-Space Linear Systems?") as tracker:
            self.play(Write(text), run_time=tracker.duration)

        with self.voiceover(text="In Modern Control Theory, <bookmark mark='A'/>we define systems as <bookmark mark='B'/>an input 'U', <bookmark mark='C'/>a state 'X', <bookmark mark='D'/>and an output 'Y'.") as tracker:
            self.play(text.animate.to_edge(UP, buff=5), run_time=tracker.time_until_bookmark("A"))
            
            state_box = Square(side_length=2, color=BLUE)
            self.play(FadeIn(state_box), run_time=tracker.time_until_bookmark("B"))

            input_arrow = Arrow(start=LEFT*4, end=LEFT, color=WHITE)
            input_label = MathTex(r"u(t)").next_to(input_arrow, UP, buff=0.1)
            self.play(FadeIn(input_arrow, shift=RIGHT), FadeIn(input_label, shift=RIGHT), run_time=tracker.time_until_bookmark("C"))

            state_label = MathTex(r"x(t)").move_to(state_box.get_center())
            self.play(FadeIn(state_label, shift=DOWN), run_time=tracker.time_until_bookmark("D"))

            output_arrow = Arrow(start=RIGHT, end=RIGHT*4, color=WHITE)
            output_label = MathTex(r"y(t)").next_to(output_arrow, UP, buff=0.1)
            self.play(FadeIn(output_arrow, shift=LEFT), FadeIn(output_label, shift=LEFT))

            self.wait(0.5)
            self.play(*[FadeOut(mob) for mob in self.mobjects], scale=0.5)


        with self.voiceover(text="""There are two equations for State-Space Linear Systems. <bookmark mark='A'/>In continuous time, <bookmark mark='B'/>meaning when time is an element of of all the numbers from zero to infinity with no breaks, <bookmark mark='C'/>the equations look like this. <bookmark mark='D'/>These matrices are called the System Parameters.""") as tracker:

            title = Text("Two Equations", font_size=40)
            self.play(Write(title), run_time=tracker.time_until_bookmark("A"))

            continuous_label = Text("Continuous-Time", font_size=40, color=YELLOW).move_to(title.get_center())
            self.play(Transform(title, continuous_label), run_time=tracker.time_until_bookmark("B"))

            time_set = MathTex(r"t \in [0, \infty)", font_size=48).next_to(title, DOWN, buff=0.7)
            self.play(Write(time_set), run_time=tracker.time_until_bookmark("C"))

            state_eq = MathTex(r"\dot{x}(t) = ", r"A(t)", r"x(t) + ", r"B(t)", r"u(t)", font_size=40)
            output_eq = MathTex(r"y(t) = ", r"C(t)", r"x(t) + ", r"D(t)", r"u(t)", font_size=40)
            equations = VGroup(state_eq, output_eq).arrange(DOWN, buff=1).move_to(ORIGIN)

            self.play(FadeOut(title), FadeOut(time_set), FadeIn(equations), run_time=tracker.time_until_bookmark("D"))

            param_label = Text("System Parameters", font_size=32, color=BLUE).next_to(equations, DOWN, buff=0.7)
            param_boxes = VGroup(
                SurroundingRectangle(state_eq[1], color=BLUE, buff=0.05),
                SurroundingRectangle(state_eq[3], color=BLUE, buff=0.05),
                SurroundingRectangle(output_eq[1], color=BLUE, buff=0.05),
                SurroundingRectangle(output_eq[3], color=BLUE, buff=0.05),
            )
            self.play(Create(param_boxes), Write(param_label))

            self.wait(0.5)
            self.play(*[FadeOut(mob) for mob in self.mobjects])


        with self.voiceover(text="If you want to learn more, check the linked video.") as tracker:
            outro_text = Text("Full Video Linked Below", font_size=36, color=YELLOW)
            link_arrow = Arrow(start=UP, end=DOWN, color=WHITE).next_to(outro_text, DOWN, buff=0.5)
            self.play(Write(outro_text), GrowArrow(link_arrow), run_time=tracker.duration)

            self.wait(1)
            self.play(*[FadeOut(mob) for mob in self.mobjects])