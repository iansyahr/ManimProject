from manim import *

config.background_color = '#0f0e17'
class LetakPerutUjungTerikat(MovingCameraScene):
    def construct(self):

        #Main Sine_graph
        time = ValueTracker(PI)
        sine_function = lambda x: (2*np.sin(x)*np.cos(time.get_value()))
        sine_graph = always_redraw(lambda: FunctionGraph(sine_function,color=BLUE, x_range=[-4*PI, 0]))

        #Dashed-Line Sine_graph
        time1 = ValueTracker(2*PI)
        sine_function1 = lambda x: (2*np.sin(x)*np.cos(time1.get_value()))
        sine_graph1 = always_redraw(lambda: DashedVMobject(FunctionGraph(sine_function1,color=BLUE, x_range=[-4*PI, 0]),num_dashes=100,dashed_ratio = 0.5))

        #Plot Sine_graph to NumberPlane() for apply get_area()
        hai = NumberPlane().set_stroke(opacity = 0)
        area_function = lambda x: (2*np.sin(x)*np.cos(PI))
        correct = hai.plot(area_function,color=BLUE, x_range=[-4*PI,0]).set_stroke(opacity = 0)
        area = hai.get_area(correct, x_range=[-PI/2,0],color = YELLOW)
        area1 = hai.get_area(correct, x_range=[-PI,-PI/2],color = RED)
        area2 = hai.get_area(correct, x_range=[-3*PI/2,-PI],color = RED)
        area3 = hai.get_area(correct, x_range=[-2*PI,-3*PI/2],color = YELLOW)
        area4 = hai.get_area(correct, x_range=[-5*PI/2,-2*PI],color = YELLOW)
        area5 = hai.get_area(correct, x_range=[-3*PI,-5*PI/2],color = RED)
        area6 = hai.get_area(correct, x_range=[-7*PI/2,-3*PI],color = RED)

        #Barrier for Sine_graph with Line()
        LineKanan = Line(start = UP*2.5,end = DOWN*2.5).set_color(RED)
        LineKiri = DashedLine(start = UP*2.5 + LEFT*4*PI,end = DOWN*2.5 + LEFT*4*PI).set_color(RED)

        #Legend for Dot, S (Simpul), and P(Perut)
        s= VGroup(*[Dot(radius = 0.15).shift(i*PI*LEFT) for i in range(0,5)]).set_color(BLUE)
        st= VGroup(*[Tex("S").shift(i*PI*LEFT + UP*0.5) for i in range(0,5)]).set_color(WHITE)
        p = VGroup(*[Tex("P").shift((2*i - 1)/2*PI*LEFT + UP*2.5) for i in range(1,5)])

        #Function
        def func(x):
          return 2*np.sin(x)*np.cos(PI)

        #Dot
        t_dot = ValueTracker()
        initial_point = [hai.coords_to_point(t_dot.get_value(), func(t_dot.get_value()))]
        dot = Dot(point=initial_point, color=ORANGE, radius = 0.15)
        dot.add_updater(lambda x: x.move_to(hai.c2p(t_dot.get_value(), func(t_dot.get_value()))))

        #Path
        path = VMobject().set_color(ORANGE).set_stroke(width=8)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
          previous_path = path.copy()
          previous_path.add_points_as_corners([dot.get_center(),dot.get_center()])
          path.become(previous_path)
        path.add_updater(update_path)

        #Perut Legend
        perut_list = BulletedList(r"Perut pertama = $\frac{1}{4} \lambda$",
                                  r"Perut kedua = $3 \times \frac{1}{4} \lambda = \frac{3}{4} \lambda$",
                                  r"Perut ketiga = $5 \times \frac{1}{4} \lambda = \frac{5}{4} \lambda$",
                                  r"Perut keempat = $7 \times \frac{1}{4} \lambda = \frac{7}{4} \lambda$",
                                  dot_scale_factor=0).shift(DOWN*5.5+LEFT*4*PI).scale(1.2)

        #Brace
        br = Brace(area, sharpness=0.1)
        lambda_text = Tex(r"$x = \frac{1}{4} \lambda$").next_to(br, DOWN)


        self.camera.frame.shift(LEFT*2*PI).scale(1.2)
        self.play(AnimationGroup(Create(sine_graph),
                                 Create(sine_graph1),
                                 Create(LineKanan),
                                 Create(LineKiri),
                                 Write(s),
                                 Create(st),
                                 Write(p),lag_ratio = 0.1))
        self.play(FadeOut(sine_graph1),
                  FadeOut(s),
                  FadeOut(st),
                  p[1].animate.shift(DOWN*2.5*2),
                  p[3].animate.shift(DOWN*2.5*2))
        self.play(Create(hai),run_time = 0.1)
        self.add(path)
        self.play(FadeIn(dot),run_time=0.5)
        self.play(self.camera.frame.animate.move_to(LEFT*2*PI+DOWN*2.5).scale(1.3))
        self.play(Create(correct),
                  GrowFromEdge(area, DR),
                  t_dot.animate.set_value(-PI/2),
                  Write(br),
                  Write(lambda_text),Write(perut_list[0]),run_time = 1)
        self.wait()
        self.play(GrowFromEdge(area1,UR),
                  GrowFromEdge(area2,UR),
                  t_dot.animate.set_value(-3*PI/2),Write(perut_list[1]),run_time = 1)
        self.wait()
        self.play(GrowFromEdge(area3,DR),
                  GrowFromEdge(area4,DR),
                  t_dot.animate.set_value(-5*PI/2),Write(perut_list[2]),run_time = 1)
        self.wait()
        self.play(GrowFromEdge(area5,UR),
                  GrowFromEdge(area6,UR),
                  t_dot.animate.set_value(-7*PI/2),Write(perut_list[3]),run_time = 1)
        self.wait(2)
