from manim import *

# Global high-contrast styling for YouTube thumbnails
BG_COLOR = "#0F111A"      # Deep matte dark blue/gray
TEXT_YELLOW = "#FFD700"   # Bright gold
TEXT_CYAN = "#00F0FF"     # Electric neon cyan
TEXT_RED = "#FF3E3E"      # Energetic red
TEXT_WHITE = "#FFFFFF"

class Thumbnail1OpenBox(Scene):
    """
    Thumbnail 1: "OPEN THE BLACK BOX!"
    Features a dark "Black Box" splitting open with glowing matrix equations pouring out.
    """
    def construct(self):
        # 1. Dark Background
        bg = Rectangle(width=16, height=9, fill_color=BG_COLOR, fill_opacity=1)
        self.add(bg)

        # 2. Main High-Impact Titles (Top & Bottom)
        title_top = Text("OPEN THE", font="Impact", color=TEXT_WHITE).scale(2.2)
        title_top.to_edge(UP, buff=0.8)
        
        title_bottom = Text("BLACK BOX!", font="Impact", color=TEXT_YELLOW).scale(2.6)
        title_bottom.to_edge(DOWN, buff=0.6)
        
        # Add slight dark drop shadows for readability
        shadow_top = title_top.copy().set_color(BLACK).shift(DOWN*0.08 + RIGHT*0.08)
        shadow_bottom = title_bottom.copy().set_color(BLACK).shift(DOWN*0.08 + RIGHT*0.08)
        self.add(shadow_top, shadow_bottom, title_top, title_bottom)

        # 3. The "Black Box" splitting open
        # Left Half of the Box
        box_left = Polygon(
            [-2, 1.2, 0], [-0.1, 1.2, 0], 
            [-0.5, -1.2, 0], [-2, -1.2, 0],
            color=TEXT_RED, fill_color="#1E0808", fill_opacity=0.9, stroke_width=8
        )
        # Right Half of the Box
        box_right = Polygon(
            [0.1, 1.2, 0], [2, 1.2, 0], 
            [2, -1.2, 0], [-0.3, -1.2, 0],
            color=TEXT_RED, fill_color="#1E0808", fill_opacity=0.9, stroke_width=8
        )
        
        # Pull them slightly apart to simulate "opening"
        box_left.shift(LEFT * 0.4)
        box_right.shift(RIGHT * 0.4)
        
        question_mark = Text("?", font="Impact", color=TEXT_RED).scale(3).move_to(ORIGIN)
        self.add(box_left, box_right, question_mark)

        # 4. Glowing Equations exploding out of the rift
        eq1 = MathTex(r"\dot{x} = Ax + Bu", color=TEXT_CYAN).scale(1.3)
        eq1.move_to(LEFT * 4 + UP * 0.2).rotate(15 * DEGREES)
        
        eq2 = MathTex(r"y = Cx + Du", color="#00FF66").scale(1.3)
        eq2.move_to(RIGHT * 4 + DOWN * 0.2).rotate(-15 * DEGREES)
        
        # Decorative arrows representing flowing signals
        arrow_l = Arrow(start=LEFT*1.5, end=LEFT*3.5, color=TEXT_CYAN, stroke_width=6)
        arrow_r = Arrow(start=RIGHT*1.5, end=RIGHT*3.5, color="#00FF66", stroke_width=6)

        self.add(eq1, eq2, arrow_l, arrow_r)


class Thumbnail2ThermostatDrone(Scene):
    """
    Thumbnail 2: "HOW WE CONTROL DRONES"
    A clean, split-screen comparison layout: Thermostat vs. Drone.
    """
    def construct(self):
        # 1. Background and Splitter
        bg = Rectangle(width=16, height=9, fill_color=BG_COLOR, fill_opacity=1)
        splitter = Line(UP * 4.5, DOWN * 4.5, color=GRAY, stroke_width=4).set_opacity(0.3)
        self.add(bg, splitter)

        # 2. Main Header Band
        header_bg = Rectangle(width=16, height=1.8, fill_color=BLACK, fill_opacity=0.8)
        header_bg.to_edge(UP, buff=0)
        header_text = Text("HOW WE CONTROL DRONES", font="Impact", color=TEXT_YELLOW).scale(1.2)
        header_text.move_to(header_bg.get_center())
        self.add(header_bg, header_text)

        # 3. Left Side: Thermostat (SISO System)
        left_center = LEFT * 3.8 + DOWN * 0.5
        
        # Draw a Thermostat
        thermo_outer = RoundedRectangle(corner_radius=0.3, width=2.2, height=3.0, color=GRAY_A, fill_color="#181B22", fill_opacity=1)
        thermo_outer.move_to(left_center)
        thermo_display = Circle(radius=0.8, color=TEXT_CYAN, fill_color=BLACK, fill_opacity=1).move_to(left_center + UP * 0.3)
        temp_val = Text("72°", font="Arial", color=TEXT_CYAN).scale(0.8).move_to(thermo_display.get_center())
        
        label_left = Text("SIMPLE (SISO)", font="Arial Black", color=TEXT_WHITE).scale(0.8)
        label_left.next_to(thermo_outer, DOWN, buff=0.4)
        
        self.add(thermo_outer, thermo_display, temp_val, label_left)

        # 4. Right Side: Drone (MIMO System)
        right_center = RIGHT * 3.8 + DOWN * 0.5
        
        # Draw an abstract Drone
        drone_body = Circle(radius=0.4, color=TEXT_RED, fill_color=BLACK, fill_opacity=1).move_to(right_center)
        arm_ul = Line(right_center, right_center + UP*0.8 + LEFT*0.8, color=GRAY_A, stroke_width=6)
        arm_ur = Line(right_center, right_center + UP*0.8 + RIGHT*0.8, color=GRAY_A, stroke_width=6)
        arm_dl = Line(right_center, right_center + DOWN*0.8 + LEFT*0.8, color=GRAY_A, stroke_width=6)
        arm_dr = Line(right_center, right_center + DOWN*0.8 + RIGHT*0.8, color=GRAY_A, stroke_width=6)
        
        rotor_ul = Ellipse(width=0.8, height=0.2, color=TEXT_CYAN).move_to(right_center + UP*0.8 + LEFT*0.8)
        rotor_ur = Ellipse(width=0.8, height=0.2, color=TEXT_CYAN).move_to(right_center + UP*0.8 + RIGHT*0.8)
        rotor_dl = Ellipse(width=0.8, height=0.2, color=TEXT_CYAN).move_to(right_center + DOWN*0.8 + LEFT*0.8)
        rotor_dr = Ellipse(width=0.8, height=0.2, color=TEXT_CYAN).move_to(right_center + DOWN*0.8 + RIGHT*0.8)
        
        # Overlay visual vector forces (glowing arrows)
        f1 = Arrow(rotor_ul.get_center(), rotor_ul.get_center() + UP*1.0, color="#00FF66", stroke_width=5)
        f2 = Arrow(rotor_ur.get_center(), rotor_ur.get_center() + UP*0.6, color="#00FF66", stroke_width=5)
        f3 = Arrow(rotor_dl.get_center(), rotor_dl.get_center() + UP*0.8, color="#00FF66", stroke_width=5)
        f4 = Arrow(rotor_dr.get_center(), rotor_dr.get_center() + UP*1.1, color="#00FF66", stroke_width=5)

        label_right = Text("COMPLEX (MIMO)", font="Arial Black", color=TEXT_RED).scale(0.8)
        label_right.next_to(drone_body, DOWN, buff=1.4)

        self.add(
            arm_ul, arm_ur, arm_dl, arm_dr, 
            rotor_ul, rotor_ur, rotor_dl, rotor_dr, 
            drone_body, f1, f2, f3, f4, label_right
        )


class Thumbnail3MathOfApollo(Scene):
    """
    Thumbnail 3: "THE MATH OF APOLLO"
    Retro 1960s blueprint aesthetic with a modern state-space matrix equation overlay.
    """
    def construct(self):
        # 1. Blueprint Grid Background (Subtle & Faded)
        bg = Rectangle(width=16, height=9, fill_color="#0A192F", fill_opacity=1)
        self.add(bg)
        
        grid = NumberPlane(
            x_range=[-10, 10, 1], 
            y_range=[-6, 6, 1],
            # Style the background grid lines to be thinner and highly transparent
            background_line_style={
                "stroke_color": "#172A45", 
                "stroke_width": 1,         # Thinned from 2 to 1
                "stroke_opacity": 0.25     # Faded from 0.6 to 0.25
            },
            # Style the main central X and Y axes so they don't pop out
            axis_config={
                "stroke_color": "#172A45",
                "stroke_width": 1.5,       # Make the main axes barely thicker than the grid
                "stroke_opacity": 0.35,    # Keep them highly transparent
                "include_ticks": False,    # Remove tick marks for a cleaner look
            }
        )
        self.add(grid)

        # 2. Main Impact Headline
        headline = Text("THE MATH OF APOLLO", font="Impact", color=TEXT_YELLOW).scale(1.8)
        headline.to_edge(UP, buff=0.6)
        
        # Text drop shadow
        headline_shadow = headline.copy().set_color(BLACK).shift(DOWN*0.06 + RIGHT*0.06)
        self.add(headline_shadow, headline)

        # 3. Stylized Apollo Rocket Blueprint (Left Side)
        rocket_pos = LEFT * 4 + DOWN * 0.5
        
        # Rocket Body
        body = Rectangle(width=1.2, height=3.2, color=TEXT_WHITE, stroke_width=4).move_to(rocket_pos)
        nose_cone = Polygon(
            rocket_pos + UP*1.6 + LEFT*0.6, 
            rocket_pos + UP*1.6 + RIGHT*0.6, 
            rocket_pos + UP*2.8, 
            color=TEXT_WHITE, stroke_width=4
        )
        fin_l = Polygon(
            rocket_pos + DOWN*1.6 + LEFT*0.6,
            rocket_pos + DOWN*1.6 + LEFT*1.2,
            rocket_pos + DOWN*0.8 + LEFT*0.6,
            color=TEXT_WHITE, stroke_width=4
        )
        fin_r = Polygon(
            rocket_pos + DOWN*1.6 + RIGHT*0.6,
            rocket_pos + DOWN*1.6 + RIGHT*1.2,
            rocket_pos + DOWN*0.8 + RIGHT*0.6,
            color=TEXT_WHITE, stroke_width=4
        )
        # Flame Thrust
        flame = Polygon(
            rocket_pos + DOWN*1.6 + LEFT*0.4,
            rocket_pos + DOWN*1.6 + RIGHT*0.4,
            rocket_pos + DOWN*2.6,
            color=TEXT_RED, fill_color=TEXT_RED, fill_opacity=0.6, stroke_width=2
        )
        
        self.add(flame, body, nose_cone, fin_l, fin_r)

        # 4. Large, Glowing State-Space Matrix Equation (Right Side)
        math_pos = RIGHT * 2.2 + DOWN * 0.3
        
        # High contrast LaTeX State Equation Matrix
        equation = MathTex(
            r"\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix}", 
            r"=", 
            r"\begin{bmatrix} 0 & 1 \\ -a & -b \end{bmatrix}", 
            r"\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}", 
            r"+", 
            r"\begin{bmatrix} 0 \\ c \end{bmatrix}", 
            r"u"
        ).scale(1.4)
        
        # Color code elements of the matrix to make it look professional and engaging
        equation[0].set_color(TEXT_CYAN)    # State derivatives
        equation[2].set_color(TEXT_YELLOW)  # System Matrix A
        equation[3].set_color(TEXT_CYAN)    # States x
        equation[5].set_color(TEXT_RED)     # Input Matrix B
        equation[6].set_color("#00FF66")    # Input u
        
        equation.move_to(math_pos)
        
        # Matrix Label tags
        label_a = Text("A MATRIX", font="Arial Black", color=TEXT_YELLOW).scale(0.5).next_to(equation[2], UP, buff=0.4)
        label_b = Text("B MATRIX", font="Arial Black", color=TEXT_RED).scale(0.5).next_to(equation[5], UP, buff=0.4)
        
        self.add(equation, label_a, label_b)