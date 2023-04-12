from manim import *

class BedaFase(MovingCameraScene):
  def construct(self):
    ax = NumberPlane((0,16),(-3,3),background_line_style={"stroke_opacity": 0}).scale(0.8)
    time = ValueTracker(0)
    function = lambda x: -2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*x)
    sin = always_redraw(lambda: ax.plot(function, color=RED))

    cir = Circle(radius = 0.15,color = BLUE, fill_opacity=1)
    cir2 = Circle(radius = 0.15,color = BLUE,fill_opacity=1)
    cir.add_updater(lambda y: y.move_to(ax.c2p(3,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*3))))
    cir2.add_updater(lambda y: y.move_to(ax.c2p(11,-2*np.sin(((2*PI)/5)*time.get_value()-((2*PI)/8)*11))))

    line = DashedLine(start = ax.c2p(3,0),end = ax.c2p(3,1.41))
    line2 = DashedLine(start = ax.c2p(11,0),end = ax.c2p(11,1.41))

    #Garis Pengukur
    garisdash = DashedLine(start = ax.c2p(0.1,0),end = ax.c2p(3,0))
    garis_kiri = Line(start = UP*0.15,end = DOWN*0.15).next_to(garisdash,LEFT,buff = 0)
    garis_kanan = Line(start = UP*0.15,end = DOWN*0.15).next_to(garisdash,RIGHT,buff = 0)
    garis_ukur = VGroup(garisdash,garis_kiri,garis_kanan).shift(DOWN*0.5)

    garisdash2 = DashedLine(start = ax.c2p(0.1,0),end = ax.c2p(11,0))
    garis_kiri2 = Line(start = UP*0.15,end = DOWN*0.15).next_to(garisdash2,LEFT,buff = 0)
    garis_kanan2 = Line(start = UP*0.15,end = DOWN*0.15).next_to(garisdash2,RIGHT,buff = 0)
    garis_ukur2 = VGroup(garisdash2,garis_kiri2,garis_kanan2).shift(DOWN*0.5)

    #Tex
    x1 = MathTex("x_1").add_updater(lambda m: m.next_to(garis_ukur, DOWN))
    x2 = MathTex("x_2").add_updater(lambda m: m.next_to(garis_ukur2, DOWN))
    P_text = MathTex("P").add_updater(lambda m: m.next_to(cir, UP))
    Q_text = MathTex("Q").add_updater(lambda m: m.next_to(cir2, UP))

    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{upgreek,scalerel}")

    rumus1 = MathTex(r"\Delta \upvarphi",r" = \upvarphi_{\scaleto{P}{3.5pt}} - \upvarphi_{\scaleto{Q}{3.5pt}}",tex_template=myTemplate)
    rumus2 = MathTex(r"\Delta \upvarphi",r"= \left( {t \over T} - {x_{\scaleto{1}{3.5pt}} \over \lambda} \right) - \left( {t \over T} - {x_{\scaleto{2}{3.5pt}} \over \lambda} \right)",tex_template=myTemplate)
    rumus3 = MathTex(r"\Delta \upvarphi",r"= {x_{\scaleto{2}{3.5pt}} - x_{\scaleto{1}{3.5pt}} \over \lambda}",tex_template=myTemplate)
    rumus4 = MathTex(r"\Delta \upvarphi",r"= {\Delta x \over \lambda}",tex_template=myTemplate)
    rumus2[0].set_opacity(0)
    rumus3[0].set_opacity(0)
    beda_fase_all = VGroup(rumus1,rumus2,rumus3,rumus4).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT*14.2).scale(1.9)
    kotak_beda_fase = SurroundingRectangle(rumus4)
    beda_fase_text = Tex("Beda Fase").scale(1.5).next_to(sin, UP*4)

    pembatas = Line(start = RIGHT*7+UP*15,end = RIGHT*7+DOWN*15)

    #self.add(NumberPlane())
    self.play(FadeIn(ax,shift = RIGHT),Create(sin),Write(beda_fase_text))
    self.play(Create(line),GrowFromCenter(cir),Write(P_text))
    self.play(GrowFromCenter(garis_ukur),Write(x1))
    self.play(Create(line2),GrowFromCenter(cir2),Write(Q_text))
    self.play(garis_ukur.animate.shift(DOWN*0.5),GrowFromCenter(garis_ukur2),Write(x2))
    self.play(self.camera.frame.animate.shift(RIGHT*7).scale(2),Create(pembatas))
    self.play(Write(beda_fase_all))
    self.play(Create(kotak_beda_fase))
    self.wait(5)
    #self.play(time.animate(run_time=7,rate_func=linear).set_value(20))