from manim import *

class GelStasionerLooseRope(MovingCameraScene):
    def construct(self):
        tracker = ValueTracker(-20)

        s = -PI/2.3
        sine_function = lambda x: (1*np.exp(-((2*x+s)-tracker.get_value())**2)-1*np.exp(-((2*x-s)-tracker.get_value())**2) + 1*np.exp(-((2*x-s)+tracker.get_value())**2)-1*np.exp(-((2*x+s)+tracker.get_value())**2))
        sine_graph = always_redraw(lambda: FunctionGraph(
            sine_function,
            color=BLUE, x_range=[-8, 0]
        ))
        Tiang = Line(start = DOWN*2.5, end = UP*2.5,color=RED).set_stroke(width = 10)
        bruh = Axes(x_range=[0, 2*PI], y_range=[-1.5, 1.5, 1])
        plan = NumberPlane()
        dot_moving = Circle(color=YELLOW,radius=0.15, fill_opacity = 1, fill_color = BLUE)

        self.add(Tiang,sine_graph,dot_moving)
        self.camera.frame.scale(0.8).move_to(LEFT*4)
        dot_moving.add_updater(lambda z: z.set_y((1*np.exp(-(s-tracker.get_value())**2)-1*np.exp(-(s+tracker.get_value())**2))+(1*np.exp(-(s-tracker.get_value())**2)-1*np.exp(-(s+tracker.get_value())**2))))
        self.play(tracker.animate(run_time=7,rate_func=linear).set_value(20))