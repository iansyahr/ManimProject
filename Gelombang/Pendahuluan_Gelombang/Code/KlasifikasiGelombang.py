from manim import *
config.background_color = "#0d0c1a"
class KlasifikasiGelombang(Scene):
  def construct(self):
    Text_KG = Text("KLASIFIKASI GELOMBANG", font="Rubik",weight = ULTRABOLD,font_size=50)
    Cir_Medium = Circle(radius = 1.5).shift(LEFT*4.6)
    Cir_ArahGetar = Circle(radius = 1.5)
    Cir_Amplitudo = Circle(radius = 1.5).shift(RIGHT*4.6)
    fon_ket = 30
    Text_Medium = Text("Medium Rambat", font="Rubik",weight = ULTRABOLD,font_size=fon_ket).next_to(Cir_Medium,DOWN)
    Text_ArahGetar = Text("Arah Getar & Rambat", font="Rubik",weight = ULTRABOLD,font_size=fon_ket).next_to(Cir_ArahGetar,DOWN)
    Text_Amplitudo = Text("Amplitudo", font="Rubik",weight = ULTRABOLD,font_size=fon_ket).next_to(Cir_Amplitudo,DOWN)

    #Medium
    medium_land = NumberPlane(x_range=(-1, 1, 1),y_range=(- 1, 1, 1)).set_opacity(0).next_to(Cir_Medium,ORIGIN)
    medium_func = lambda x : 0.5*np.sin(-6*x)
    medium_sinus = medium_land.plot(medium_func,x_range=[-PI/3, PI/3]).set_color(BLUE).set_stroke(width = 10)
    medium_objek = ImageMobject("/content/ManimProject/Gelombang/Pendahuluan_Gelombang/kotaktransparan.png").set_color(WHITE).scale(0.5).next_to(medium_land,ORIGIN)

    #ArahGetarNRambat
    getar_land = NumberPlane(x_range=(-1, 1, 1),y_range=(- 1, 1, 1),background_line_style={"stroke_opacity": 0}).scale(1.2)
    getar_func = lambda x : 0.5*np.sin(-6*x)
    getar_ob = getar_land.plot(getar_func,x_range=[-PI/6, PI/6]).set_color(BLUE).set_stroke(width = 8)
    getar_ob_1 = getar_land.plot(getar_func,x_range=[-PI/6, PI/6]).set_stroke(opacity = 0)
    dot_getar = Dot(radius = 0.1).set_color(ORANGE).scale(1.2)
    panah_1 = Arrow(start = getar_land.c2p(PI/6,0), end = getar_land.c2p(PI/6,0.5), buff =0).set_color(GREEN)
    panah_2 = Arrow(start = getar_land.c2p(PI/6,0), end = getar_land.c2p(((PI/6)+0.5),0), buff =0).set_color(GREEN)

    #Amplitudo
    amp_land = NumberPlane(x_range=(-1, 1, 1),y_range=(- 1, 1, 1),background_line_style={"stroke_opacity": 0}).scale(1.2).next_to(Cir_Amplitudo, ORIGIN)
    dot_amp = Dot(radius = 0.1).shift(amp_land.c2p(0,0.5)).set_color(GREEN)
    text_amp = Tex("A").next_to(dot_amp,UP*0.1+RIGHT*0.5).scale(0.8)
    amp_func = lambda x : 0.5*np.cos(-6*x)
    amp_ob = amp_land.plot(amp_func).set_color(BLUE).set_stroke(width = 8)

    #self.add(NumberPlane())
    self.play(FadeIn(Text_KG, shift = UP))
    self.wait()
    self.play(Text_KG.animate.shift(UP*3).scale(0.7))
    self.add(medium_land)
    self.play(AnimationGroup(Create(Cir_Medium),
                             AnimationGroup(Create(medium_sinus),FadeIn(medium_objek)),
                             FadeIn(Text_Medium,shift = DOWN*0.25),
                             AnimationGroup(Create(Cir_ArahGetar),Create(getar_ob_1),Create(getar_land)),
                             FadeIn(dot_getar),AnimationGroup(Create(getar_ob),MoveAlongPath(dot_getar, getar_ob_1),run_time =0.97),
                             AnimationGroup(GrowArrow(panah_1),GrowArrow(panah_2),FadeIn(Text_ArahGetar,shift = DOWN*0.25)),
                             AnimationGroup(Create(Cir_Amplitudo),Create(amp_land)),
                             AnimationGroup(Create(amp_ob),Create(dot_amp),Write(text_amp)),
                             FadeIn(Text_Amplitudo,shift = DOWN*0.25),
                             lag_ratio = 0.3))
    self.wait()    
