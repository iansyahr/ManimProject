from manim import *

class ArahRambat(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 2*PI], y_range=[-1.5, 1.5, 1], axis_config={"include_tip": True, "stroke_width":10}
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
        
        yellowbox = Rectangle(color = YELLOW, height = 3.8, width=6.6)
        yellowbox.shift(RIGHT*3.5 + UP*2)

        ArahRambatTex = Text("Arah Getar & Arah Rambat", font_size = 35)
        ArahRambatTex.shift(RIGHT*2.5 + UP*2)
        
        self.add(plane)
        self.play(AnimationGroup(Create(ax),Create(labels),Create(graph),Create(dot),Write(ArahRambatTex),lag_ratio = 0, run_time = 1))
        self.play(t.animate.set_value(PI/2),run_time= 0.7)
        
        arrow = Arrow(dot.get_center(), [-3,3.2,0], buff=0, stroke_width= 10)
        arrow1 = Arrow(dot.get_center(), [-1.8,2,0], buff=0, stroke_width= 10)
        dotgan = Dot([-3,2,0], radius=0.15)
        da = VGroup(arrow,arrow1)
        all = VGroup(da,ax,labels,graph,dotgan,ArahRambatTex)

        self.play(GrowFromPoint(da, dot),run_time=0.5)
        self.play(AnimationGroup(FadeIn(dotgan),FadeOut(dot),lag_ratio = 0, run_time = 0.1))
        self.play(AnimationGroup(all.animate(lag_ratio = 0, run_time = 1).scale(0.5).shift(RIGHT*3.5 + UP*1.5),Create(yellowbox), lag_ratio=0))
        self.wait(2)
