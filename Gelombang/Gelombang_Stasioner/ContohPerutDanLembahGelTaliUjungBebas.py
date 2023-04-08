from manim import *
class ContohPerutDanLembahGelTaliUjungBebas(MovingCameraScene):
    def construct(self):
        time = ValueTracker(PI/2)

        sine_function = lambda x: (2*np.cos(x)*np.sin(time.get_value()))
        sine_graph = always_redraw(lambda: FunctionGraph(sine_function,color=BLUE, x_range=[-4*PI, 0]))

        time1 = ValueTracker(PI/2)
        sine_function1 = lambda x: (2*np.cos(x)*np.sin(time1.get_value()))
        sine_graph1 = always_redraw(lambda: DashedVMobject(FunctionGraph(sine_function1,color=BLUE, x_range=[-4*PI, 0]),num_dashes=100,dashed_ratio = 0.5))

        #bruh = Axes(x_range=[0, 2*PI], y_range=[-1.5, 1.5, 1])
        LineKanan = Line(start = UP*2.5,end = DOWN*2.5).set_color(RED)
        LineKiri = DashedLine(start = UP*2.5 + LEFT*4*PI,end = DOWN*2.5 + LEFT*4*PI).set_color(RED)
        plan = NumberPlane()

        s= VGroup(*[Dot(radius = 0.15).shift((2*i - 1)/2*PI*LEFT) for i in range(1,5)]).set_color(BLUE)
        st= VGroup(*[Tex("S").shift((2*i - 1)/2*PI*LEFT + UP*0.5) for i in range(1,5)]).set_color(WHITE)

        p = VGroup(*[Tex("P").shift(i*PI*LEFT + UP*2.5) for i in range(0,5)])

        #self.add(plan)
        #time with cairo is 1 minute
        self.camera.frame.shift(LEFT*2*PI).scale(1.2)
        self.play(AnimationGroup(Create(sine_graph),Create(LineKanan),Create(LineKiri)))
        self.play(time.animate(run_time=3,rate_func=linear).set_value(9*PI/2))
        self.play(Create(sine_graph1),run_time = 0.1)
        self.play(time1.animate(run_time=1,rate_func=linear).set_value(3*PI/2))
        self.play(Create(s),Write(st))
        self.play(Write(p))
        self.wait(1)