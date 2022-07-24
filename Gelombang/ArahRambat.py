from manim import *

class ArahRambat(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 2*PI], y_range=[-1.5, 1.5, 1], axis_config={"include_tip": True}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        t = ValueTracker(0)

        def func(x):
            return np.sin(x)
        graph = ax.plot(func, color=WHITE,stroke_width = 10)


        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point, color=WHITE, radius=0.15)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        plane = NumberPlane()

        self.play(AnimationGroup(Create(ax),Create(labels),Create(graph),Create(dot),lag_ratio = 0))
        self.play(t.animate.set_value(PI/2))
        
        arrow = Arrow(dot.get_center(), [-3,4,0], buff=0)
        arrow1 = Arrow(dot.get_center(), [-1,2,0], buff=0)
        da = VGroup(arrow,arrow1)

        self.play(GrowFromPoint(da, dot))
        self.wait()