from manim import *

class GelombangSeFase(MovingCameraScene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{upgreek}")
        ax = NumberPlane((0,10),(-3,3),background_line_style={"stroke_opacity": 0}).add_coordinates()
        ay = NumberPlane((0,10),(-3,3),background_line_style={"stroke_opacity": 0}).add_coordinates()
        time = ValueTracker(0)
        function = lambda x: -2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*x)
        sin = always_redraw(lambda: ax.plot(function, color=RED))
        sin1 = always_redraw(lambda: ay.plot(function, color=RED))
        #label = ax.get_graph_label(graph=sin,label= MathTex(r"\frac{\pi}{2}",font_size = 20),dot=True,direction=UR)
        cir = Circle(radius = 0.15,color = BLUE, fill_opacity = 1)
        cir1 = Circle(radius = 0.15,color = BLUE, fill_opacity = 1)
        cir2 = Circle(radius = 0.15,color = BLUE, fill_opacity = 1)
        cir3 = Circle(radius = 0.15,color = BLUE, fill_opacity = 1)
        #label.add_updater(lambda z: z.set_y(np.sin(time.get_value() - PI/2)))
        cir.add_updater(lambda y: y.move_to(ax.c2p(1,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*1))))
        cir1.add_updater(lambda y: y.move_to(ax.c2p(3,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*3))))

        cir2.add_updater(lambda y: y.move_to(ay.c2p(9,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*9))))
        cir3.add_updater(lambda y: y.move_to(ay.c2p(1,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*1))))

        label = MathTex("P").add_updater(lambda m: m.next_to(cir, UP))
        label2 = MathTex("Q").add_updater(lambda m: m.next_to(cir1, UP))
        label3 = MathTex("Q").add_updater(lambda m: m.next_to(cir2, UP))
        label4 = MathTex("P").add_updater(lambda m: m.next_to(cir3, UP))
        rumus_gelombang = MathTex(r"y=-2\sin\left(\frac{2\pi}{5}t-\frac{2\pi}{8}x\right)").shift(DOWN*1.5 + RIGHT*1.7).scale(0.5)
        rumus_gelombang1 = MathTex(r"y=-2\sin\left(\frac{2\pi}{5}t-\frac{2\pi}{8}x\right)").shift(DOWN*1.5 + RIGHT*1.7).scale(0.5)

        line = DashedLine(start = ax.c2p(0,1.41),end = ax.c2p(1,1.41))
        line.add_updater(lambda y: y.move_to(ax.c2p(0.5,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*9))))

        line1 = DashedLine(start = ax.c2p(0,1.41),end = ax.c2p(3,1.41))
        line1.add_updater(lambda y: y.move_to(ax.c2p(1.5,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*3))))

        line2 = DashedLine(start = ax.c2p(0,1.41),end = ax.c2p(9,1.41))
        line2.add_updater(lambda y: y.move_to(ay.c2p(4.5,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*9))))

        kotak = Rectangle(height=4, width= 6.5).set_color(YELLOW)

        sefase_text = Tex("Sefase").next_to(kotak,DOWN)

        def0_text = Tex(r"Dua titik gelombang disebut",r" sefase")
        def1_text = Tex(r"jika jarak kedua titik",r" berupa kelipatan bilangan bulat,")
        def2_text = Tex(r"dari",r" panjang gelombangnya")
        def_text = VGroup(def0_text,def1_text,def2_text).arrange(DOWN).shift(DOWN*3.7).scale(0.8)

        beda_fase_sefase = MathTex(r"\Delta \upvarphi = 0,1,2,3, ...",tex_template=myTemplate).next_to(def_text,DOWN*1.25)
        kotak_nofase = SurroundingRectangle(beda_fase_sefase)
   
        group = VGroup(line,line1,ax,sin,cir,cir1,label,label2).scale(0.6)
        group1 = VGroup(line2,ay,sin1,cir2,cir3,label3,label4).scale(0.6)

        #self.add(NumberPlane())

        self.play(FadeIn(group1, shift = UP*0.5),Create(kotak),FadeIn(rumus_gelombang,shift = UP*0.5),Write(sefase_text))
        self.wait(2)
        #self.play(group.animate.shift(UP))
        self.play(self.camera.frame.animate.shift(DOWN*1.9).scale(1.1))
        self.play(Write(def_text))
        self.play(def0_text.animate.set_color_by_tex("sefase", BLUE))
        self.play(def1_text.animate.set_color_by_tex("berupa kelipatan bilangan bulat", BLUE))
        self.play(def2_text.animate.set_color_by_tex("panjang gelombangnya", BLUE))
        self.play(Write(beda_fase_sefase),Create(kotak_nofase))
        self.play(time.animate(run_time=7,rate_func=linear).set_value(20))