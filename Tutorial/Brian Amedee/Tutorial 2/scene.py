from manim import *

class GraphicMovement(Scene):
    def construct(self):
        axes = Axes(x_range=[0,5,1], y_range=[0,3,1], x_length=5, y_length=3, axis_config={"include_tip": True, "numbers_to_exclude": [0]}).add_coordinates()
        axes.to_edge(UR)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        graph = axes.plot(lambda x : x**0.5, x_range=[0, 4], color=YELLOW)
        graphing_stuff = VGroup(axes, graph, axis_labels)

        self.play(DrawBorderThenFill(axes), Write(axis_labels))
        self.play(Create(graph))
        self.play(graphing_stuff.animate.shift(DOWN*4))
        self.play(axes.animate.shift(LEFT*3), run_time=3)

class Graphing(Scene):
    def construct(self):
        my_plane = NumberPlane(x_range=[-6,6], x_length=5, y_range=[-10,10], y_length=5)
        my_plane.add_coordinates()
        my_plane.shift(RIGHT*3)

        my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5), x_range=[-6,6], color=GREEN_B)

        area = my_plane.get_area(graph=my_function, x_range=[-5,5], color=[BLUE, YELLOW])

        label = MathTex("f(x)=0.1x(x-5)(x+5)").next_to(my_plane, UP, buff=0.2)

        horiz_line = Line(start=my_plane.c2p(0, my_function.underlying_function(-2)), end=my_plane.c2p(-2, my_function.underlying_function(-2)), stroke_color=YELLOW, stroke_width=10)

        self.play(DrawBorderThenFill(my_plane))
        self.play(Create(my_function), Write(label))
        self.play(FadeIn(area))
        self.play(Create(horiz_line))

class CoordinateSystem(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4,4,1], x_length=4, y_range=[0,20,5], y_length=4).add_coordinates()
        plane.shift(LEFT*3+DOWN*1.5)
        plane_graph = plane.plot(lambda x : x**2, x_range=[-4,4], color=GREEN)
        area = plane.get_riemann_rectangles(graph=plane_graph, x_range=[-2,2], dx=0.05)

        axes = Axes(x_range=[-4,4,1], x_length=4, y_range=[-20,20,5], y_length=4).add_coordinates()
        axes.shift(RIGHT*3+DOWN*1.5)
        axes_graph = axes.plot(lambda x : 2*x, x_range=[-4,4], color=YELLOW)
        v_lines = axes.get_vertical_lines_to_graph(graph=axes_graph, x_range=[-3,3], num_lines=12)

        self.play(Write(plane), Create(axes))
        self.play(Create(plane_graph), Create(axes_graph), run_time=2)
        self.add(area, v_lines)
        self.wait(3)

class Tute2(Scene):
    def construct(self):
        e = ValueTracker(0.01)

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT*2)
        graph1 = always_redraw(lambda : ParametricFunction(lambda t : plane.polar_to_point(2*np.sin(3*t), t), t_range=[0, e.get_value()], color=GREEN))
        dot1 = always_redraw(lambda : Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end()))

        axes = Axes(x_range=[0,4,1], x_length=3, y_range=[-3,3,1], y_length=3).shift(RIGHT*4)
        axes.add_coordinates()
        graph2 = always_redraw(lambda : axes.plot(lambda x : 2*np.sin(3*x), x_range=[0, e.get_value()], color=GREEN))
        dot2 = always_redraw(lambda : Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end()))

        title = MathTex(r"f( \theta ) = 2sin(3 \theta )", color=GREEN).next_to(axes, UP, buff=0.2)

        self.play(LaggedStart(Write(plane), Create(axes), Write(title), run_time=3, lag_ratio=0.5))
        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(PI), run_time=10, rate_func=linear)
        self.wait(2)