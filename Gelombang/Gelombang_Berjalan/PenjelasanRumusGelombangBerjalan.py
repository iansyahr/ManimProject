from manim import *
config.background_color = '#0f0e17'
class PenjelasanRumusGelombangBerjalan(MovingCameraScene):
  def construct(self):
    lahan = NumberPlane(x_range=(-20,20,1)).set_stroke(opacity=0)

    time = ValueTracker(0)
    w = ValueTracker(0)
    k = ValueTracker(1)
    A = ValueTracker(-1)
    sine_function = lambda x: A.get_value()*np.sin(w.get_value()*time.get_value() - k.get_value()*PI*x)
    sine_graph = always_redraw(lambda: FunctionGraph(sine_function,color=BLUE, x_range=[0,8]))

    #Cartesian
    panah_x = Arrow(start = ORIGIN, end=RIGHT*8.5,buff = 0)
    panah_y = Arrow(start = DOWN*2, end=UP*2,buff = 0)
    x_tip = MathTex("x").next_to(panah_x,RIGHT)
    y_tip = MathTex("y").next_to(panah_y,UP)
    panah = VGroup(panah_x,panah_y,x_tip,y_tip).set_color(GREY)

    #Rumus
    Rumus = MathTex("y", "=", "A", "\sin", "(","\omega", "t" ,"-", "k","x",")").shift(RIGHT*13.5+UP*4).scale(1.3)

    #Pembatas
    batas = Line(start = UP*7 + RIGHT*9.5,end = DOWN*7 + RIGHT*9.5)

    #Keterangan
    y_ket = Tex("$y$ = simpangan(m)").next_to(Rumus,DOWN)
    A_ket = Tex("$A$ = Amplitudo(m)").next_to(Rumus,DOWN)
    w_ket = Tex("$\omega$ = kecepatan sudut (rad/s)").next_to(Rumus,DOWN)
    t_ket = Tex("$t$ = waktu (s)").next_to(Rumus,DOWN)
    k_ket = Tex("$k$ = bilangan gelombang").next_to(Rumus,DOWN)
    x_ket = Tex("$x$ = jarak titik ke sumber gelombang (m)").next_to(Rumus,DOWN).scale(0.8)
    all_ket = BulletedList("$y$ = simpangan(m)",
                         "$A$ = Amplitudo(m)",
                         "$\omega$ = kecepatan sudut (rad/s)",
                         "$t$ = waktu (s)",
                         "$k$ = bilangan gelombang",
                         "$x$ = jarak titik ke","sumber gelombang (m)",dot_scale_factor=0).next_to(batas,RIGHT*2)


    #Definisi
    A_def = Paragraph("Amplitudo adalah simpangan terjauh \nyang diukur dari titik kesetimbangan \npada getaran",font_size=25).next_to(batas,RIGHT*2)
    w_def = Paragraph("Kecepatan sudut adalah besar sudut \nyang ditempuh per satuan waktu",font_size=25).next_to(Rumus,DOWN*3).next_to(batas,RIGHT*2)
    k_def = Paragraph("Bilangan gelombang didefinisikan \nsebagai jumlah radian per satuan jarak",font_size=25).next_to(Rumus,DOWN*3).next_to(batas,RIGHT*2)

    #Rumus Kecepatan Sudut dan Bilangan Gelombang
    w_rumus = MathTex(r"\omega = \frac{2 \pi}{T} = 2 \pi f").next_to(w_def,DOWN*2)
    k_rumus = MathTex(r"k = \frac{2 \pi}{\lambda}").next_to(k_def,DOWN*2)
    w_rumus_kotak = SurroundingRectangle(w_rumus)
    k_rumus_kotak = SurroundingRectangle(k_rumus)
    w_rumust = VGroup(w_rumus,w_rumus_kotak)
    k_rumust = VGroup(k_rumus,k_rumus_kotak)

    #Animasi Angka
    A_tracker = ValueTracker(1)
    A_point = Tex("$A$ = ")
    A_num = DecimalNumber().next_to(A_point,RIGHT)
    A_Anim = VGroup(A_point,A_num).next_to(sine_graph,UP)
    A_num.add_updater(lambda m: m.set_value(A_tracker.get_value()))

    w_tracker = ValueTracker(0)
    w_point = Tex("$\omega$ = ")
    w_num = DecimalNumber().next_to(w_point,RIGHT)
    w_rad = Tex("  rad/s").next_to(w_num,RIGHT)
    w_Anim = VGroup(w_point,w_num,w_rad).next_to(sine_graph,UP)
    w_num.add_updater(lambda m: m.set_value(40*np.sin(0.166666*PI*w_tracker.get_value())))

    k_point1 = MathTex(r"k","=","2","\pi").next_to(sine_graph,UP)
    k_point2 = MathTex(r"k","=","5","\pi").next_to(sine_graph,UP)
    k_point3 = MathTex(r"k","=",r"\frac{1}{2}","\pi").next_to(sine_graph,UP)
    
    #Animation Tuning
    #pesawat = NumberPlane((-20,20),(-20,20))
    #self.add(pesawat)
    self.camera.frame.shift(RIGHT*4)
    self.play(AnimationGroup(Create(panah),Create(sine_graph),lag_ratio=0.1))
    self.play(AnimationGroup(self.camera.frame.animate.shift(RIGHT*4).scale(1.3),Create(batas),Write(Rumus),lag_ratio = 0.1))
    self.wait()
    self.play(Rumus[0].animate.set_color(RED),
              Flash(Rumus[0]),
              FadeIn(y_ket,shift = LEFT)) #y
    self.wait()

    self.play(Rumus[2].animate.set_color(RED),
              Flash(Rumus[2]),
              Rumus[0].animate.set_color(WHITE),
              FadeOut(y_ket,shift = LEFT),
              FadeIn(A_ket,shift = LEFT),
              FadeIn(A_def,shift = LEFT)) #A

    self.play(Write(A_Anim))
    self.play(A.animate.set_value(-2),A_tracker.animate.set_value(2),A_Anim.animate.shift(UP))
    self.wait(0.5)
    self.play(A.animate.set_value(-1),A_tracker.animate.set_value(1),A_Anim.animate.shift(DOWN))
    self.wait()

    self.play(Rumus[5].animate.set_color(RED),
              Flash(Rumus[5]),
              Rumus[2].animate.set_color(WHITE),
              FadeOut(A_ket,shift = LEFT),
              FadeOut(A_def,shift = LEFT),
              FadeOut(A_Anim,shift = LEFT),
              FadeIn(w_ket,shift = LEFT),
              FadeIn(w_def,shift = LEFT),
              FadeIn(w_rumust,shift = LEFT)) #w

    self.play(Write(w_Anim))
    self.play(AnimationGroup(w.animate.set_value(40),time.animate.set_value(6),run_time=6),
              AnimationGroup(w_tracker.animate.set_value(6),run_time=6))
    
    self.play(Rumus[6].animate.set_color(RED),
              Flash(Rumus[6]),
              Rumus[5].animate.set_color(WHITE),
              FadeOut(w_ket,shift = LEFT),
              FadeOut(w_Anim,shift = LEFT),
              FadeOut(w_def,shift = LEFT),
              FadeOut(w_rumust,shift = LEFT),
              FadeIn(t_ket,shift = LEFT)) #t
    self.wait()
    
    self.play(Rumus[8].animate.set_color(RED),
              Flash(Rumus[8]),
              Rumus[6].animate.set_color(WHITE),
              FadeOut(t_ket,shift = LEFT),
              FadeIn(k_ket,shift = LEFT),
              FadeIn(k_def,shift = LEFT),
              FadeIn(k_rumust,shift = LEFT)) #k
    
    self.play(k.animate.set_value(2),Write(k_point1))
    self.wait(0.5)
    self.play(k.animate.set_value(5),ReplacementTransform(k_point1,k_point2))
    self.wait(0.5)
    self.play(k.animate.set_value(0.5),ReplacementTransform(k_point2,k_point3))
    self.wait()
    
    self.play(Rumus[9].animate.set_color(RED),
              Flash(Rumus[9]),
              Rumus[8].animate.set_color(WHITE),
              FadeOut(k_ket,shift = LEFT),
              FadeOut(k_point3,shift = LEFT),
              FadeOut(k_def,shift = LEFT),
              FadeOut(k_rumust,shift = LEFT),
              k.animate.set_value(1),
              FadeIn(x_ket,shift = LEFT)) #x
    self.wait()
    self.play(Rumus[9].animate.set_color(WHITE),
              FadeIn(all_ket,shift = LEFT),
              FadeOut(x_ket,shift = LEFT))
    self.wait(4)