from manim import *

class Amplitudo(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 2*PI], y_range=[-1.5, 1.5], axis_config={"include_tip": True}
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

        self.add(plane)
        self.play(AnimationGroup(Create(ax),Create(graph),lag_ratio = 0))

        arrow = Arrow([-3,0,0], [-3,2,0], buff=0)
        arrow1 = DashedLine([-3,0,0], [-3,2,0],stroke_width = 10, dash_length=0.1).add_tip()
        bulat = Dot([-3,2,0], radius=0.15)

        text = MathTex("A",font_size=70)
        text.shift([-3,2.6,0])

        self.play(AnimationGroup(GrowFromPoint(arrow1,[-3,0,0]),GrowFromCenter(bulat),Write(text),lag_ratio = 0))
        self.wait()