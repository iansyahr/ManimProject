from manim import *
class RumusFaseGelombang(MovingCameraScene):
  def construct(self):
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{upgreek}")

    plan = NumberPlane((-20,20),(-20,20))

    ukuran_font = 60

    line1 = MathTex(r"y", #0
                    "=", #1
                    "A \sin ", #2
                    "(", #3
                    "\omega", #4
                    "t", #5
                    "-", #6
                    "k", #7
                    "x", #8
                    ")",font_size=ukuran_font)
    line2 = MathTex(r"y", #0
                    "=", #1
                    r"A \sin", #2
                    r"\left(", #3
                    "{2\pi", #4
                    "\over T}", #5
                    "t", #6
                    "-", #7
                    "{2 \pi", #8
                    "\over \lambda}", #9
                    "x", #10
                    r"\right)",font_size=ukuran_font)
    line2[0].set_opacity(0)
    line3 = MathTex(r"y", #0
                    "=", #1
                    r"A \sin", #2
                    r"2 \pi", #3
                    r"\left(", #4
                    "{t", #5
                    "\over T}", #6
                    "-", #7
                    "{x", #8
                    "\over \lambda}", #9
                    r"\right)",font_size=ukuran_font) #10
    line3[0].set_opacity(0)

    w_rumus = MathTex(r"\omega = ", #0
                      r"{2 \pi", #1
                      "\over T} ", #2
                      "= 2 \pi f ").shift(UP*2+LEFT*3) #3
    w_rumus_kotak = SurroundingRectangle(w_rumus)
    k_rumus = MathTex(r"k =", #0
                      r"{2 \pi", #1
                      "\over \lambda}").shift(UP*2+RIGHT*3) #2
    k_rumus_kotak = SurroundingRectangle(k_rumus)

    wk_all = VGroup(w_rumus,w_rumus_kotak,k_rumus,k_rumus_kotak)
    rumus_all = VGroup(line1,line2,line3).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT*0.6 + DOWN*1.7)

    #self.add(plan)
    self.play(Write(line1))
    self.wait()
    self.play(FadeIn(wk_all,shift = DOWN))
    self.wait()
    self.play(self.camera.frame.animate.shift(DOWN*1.3),
              FadeOut(wk_all),
              ReplacementTransform(line1[1].copy(),line2[1]),
              ReplacementTransform(line1[2].copy(),line2[2]),
              ReplacementTransform(line1[3].copy(),line2[3]),
              ReplacementTransform(line1[9].copy(),line2[11]),
              ReplacementTransform(line1[3].copy(),line2[3]),
              ReplacementTransform(line1[6].copy(),line2[7]),
              ReplacementTransform(line1[5].copy(),line2[6]),
              ReplacementTransform(line1[8].copy(),line2[10]),
              ReplacementTransform(w_rumus[1].copy(),line2[4]),
              ReplacementTransform(w_rumus[2].copy(),line2[5]),
              ReplacementTransform(k_rumus[1].copy(),line2[8]),
              ReplacementTransform(k_rumus[2].copy(),line2[9]),)
    self.wait()
    self.play(self.camera.frame.animate.shift(DOWN*0.5),
              ReplacementTransform(line2[1].copy(),line3[1]),
              ReplacementTransform(line2[2].copy(),line3[2]),
              ReplacementTransform(line2[4].copy(),line3[3]),
              ReplacementTransform(line2[8].copy(),line3[3]),
              ReplacementTransform(line2[3].copy(),line3[4]),
              ReplacementTransform(line2[11].copy(),line3[10]),
              ReplacementTransform(line2[6].copy(),line3[5]),
              ReplacementTransform(line2[5].copy(),line3[6]),
              ReplacementTransform(line2[7].copy(),line3[7]),
              ReplacementTransform(line2[10].copy(),line3[8]),
              ReplacementTransform(line2[9].copy(),line3[9]),)
    self.wait(2)

    pembatas = Line(start = RIGHT*5+UP*10,end = RIGHT*5+DOWN*10)
    fase = MathTex(r"\upvarphi = ", #0
                   r"\left(", #1
                   "{t", #2
                   "\over T}", #3
                   "-", #4
                   "{x", #5
                   "\over \lambda}", #6
                   r"\right)",tex_template=myTemplate,font_size = 70).shift(RIGHT*9.25) #7

    sudut_fase = MathTex(r"\theta", #0
                    "=", #1
                    r"2 \pi", #2
                    r"\left(", #3
                    "{t", #4
                    "\over T}", #5
                    "-", #6
                    "{x", #7
                    "\over \lambda}", #8
                    r"\right)",font_size= 70).shift(RIGHT*9.25 + DOWN*4) #9

    sudut_fase2 = MathTex(r"\theta", #0
                    "=", #1
                    r"2 \pi", #2
                    r"\upvarphi",tex_template=myTemplate,font_size= 70).shift(RIGHT*9.25 + DOWN*4) #3

    kotak_fase = SurroundingRectangle(fase,buff = 0.3)
    kotak_sudut_fase = SurroundingRectangle(sudut_fase,buff = 0.3)
    kotak_sudut_fase2 = SurroundingRectangle(sudut_fase2,buff = 0.3)
    fase_text = Tex("Fase",font_size = 80).next_to(kotak_fase,UP)
    sudut_fase_text = Tex("Sudut Fase",font_size = 80).next_to(kotak_sudut_fase,UP)
    sudut_fase_text2 = Tex("Sudut Fase",font_size = 80).next_to(kotak_sudut_fase2,UP)
    self.play(Circumscribe(line3[4:11]))
    self.play(AnimationGroup(ReplacementTransform(line3[4:11].copy(),fase[1:8]),self.camera.frame.animate.shift(RIGHT*5).scale(1.2),Create(pembatas),Write(fase[0]),lag_ratio = 0.1))
    self.play(Create(kotak_fase))
    self.play(FadeIn(fase_text, shift = UP*0.25))
    self.play(Circumscribe(line3[3:11]))
    self.play(ReplacementTransform(line3[3:11].copy(),sudut_fase[2:10]),Write(sudut_fase[0:2]))
    self.play(Create(kotak_sudut_fase))
    self.play(FadeIn(sudut_fase_text, shift = UP*0.25))
    self.play(ReplacementTransform(sudut_fase[0:3],sudut_fase2[0:3]),
              ReplacementTransform(sudut_fase[3:10],sudut_fase2[3]),
              ReplacementTransform(kotak_sudut_fase,kotak_sudut_fase2),
              ReplacementTransform(sudut_fase_text,sudut_fase_text2))
    self.wait(2)
    #ReplacementTransform(trigo[6].copy(),line3[0])