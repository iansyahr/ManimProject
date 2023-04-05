from manim import *
#config color jangan diubah
config.background_color = "#291F00"
class GelombangMekanik_PartikelGetar(MovingCameraScene):
  def construct(self):
    time = ValueTracker(0)
    waktu = ValueTracker(0)
    lebar_mata = 0.3
    warna_mata = BLACK
    mata1 = Ellipse(width=lebar_mata, height=lebar_mata, color=warna_mata, fill_opacity=1).shift(LEFT*0.4 + UP*0.2)
    mata2 = Ellipse(width=lebar_mata, height=lebar_mata, color=warna_mata, fill_opacity=1).shift(RIGHT*0.4 + UP*0.2)
    alisleft = VMobject(stroke_width=10, color=warna_mata, joint_type = LineJointType.ROUND).set_points_as_corners([np.array([-0.3, 0.15, 0]),np.array([0, 0, 0]),np.array([-0.3, -0.15, 0]),]).shift(LEFT*0.25+ UP*0.2)
    alisright = VMobject(stroke_width=10, color=warna_mata, joint_type = LineJointType.ROUND).set_points_as_corners([np.array([0.3, 0.15, 0]),np.array([0, 0, 0]),np.array([0.3, -0.15, 0]),]).shift(RIGHT*0.25+ UP*0.2)
    mainpartikel = VGroup(mata1,mata2)
    alis = VGroup(alisleft,alisright)
    d = VGroup()
    for i in range(0,153):
      a1 = Circle(radius = 1,color="#FFC000",fill_opacity = 1)
      d.add(a1)

    d.arrange_in_grid(rows = 9,buff=0.5)
    d.add_updater(lambda z: z.set_x(0.5*np.sin(time.get_value())))

    #GELOMBANG
    tebal = ValueTracker(30)
    jari = ValueTracker(0.15)
    tebal1 = ValueTracker(30)
    jari1 = ValueTracker(0.15)
    tebal2 = ValueTracker(30)
    jari2 = ValueTracker(0.15)

    atur_posisi = LEFT*8.2
    atur_ukuran = 5
    warna_gel = WHITE

    a1 = Circle(radius=0.15,stroke_width = 30).shift(atur_posisi).scale(atur_ukuran).set_color(warna_gel)
    a1.add_updater(lambda z: z.become(Circle(radius=jari.get_value() ,stroke_width = tebal.get_value()).shift(atur_posisi).scale(atur_ukuran).set_color(warna_gel)))
    a2 = Circle(radius=0.15,stroke_width = 30).shift(atur_posisi).scale(atur_ukuran).set_color(warna_gel)
    a2.add_updater(lambda z: z.become(Circle(radius=jari1.get_value() ,stroke_width = tebal1.get_value()).shift(atur_posisi).scale(atur_ukuran).set_color(warna_gel)))
    a3 = Circle(radius=0.15,stroke_width = 30).shift(atur_posisi).scale(atur_ukuran).set_color(warna_gel)
    a3.add_updater(lambda z: z.become(Circle(radius=jari2.get_value() ,stroke_width = tebal2.get_value()).shift(atur_posisi).scale(atur_ukuran).set_color(warna_gel)))
    gelombang = VGroup(a1,a2,a3)

    #Bell
    Lens = Circle(radius = 1.2, color=BLUE_C , fill_opacity = 1).shift(UP*2 + LEFT*5).set_stroke(width = 10,color = WHITE)
    point_bell = Dot().set_opacity(0).next_to(Lens,ORIGIN)
    bell = ImageMobject("/content/ManimProject/Gelombang/Pendahuluan_Gelombang/bel_bell.png").shift(UP*2.5+LEFT*4.7).scale(0.2)
    #pemukul = ImageMobject("/content/ManimProject/Gelombang/Pendahuluan_Gelombang/bel_pemukul.png").shift(UP*1.5+LEFT*5.5).scale(0.2)
    garis_pemukul = Line(start = UP*1, end = ORIGIN).set_stroke(color=BLACK,width = 10)
    garis2_pemukul = Line(start = DOWN*1, end = ORIGIN).set_stroke(width = 10).set_opacity(0)
    kepala = Dot(color = YELLOW).next_to(garis_pemukul,UP,buff = 0)
    pemukul = VGroup(garis_pemukul,garis2_pemukul,kepala).shift(UP*1.5+LEFT*5.5)
    
    #self.add(NumberPlane())
    self.camera.frame.scale(2.5)
    self.add(d,mainpartikel)
    self.play(self.camera.frame.animate(run_time = 3).scale(1/2.5))
    mata1.add_updater(lambda z: z.become(Ellipse(width=lebar_mata, height=lebar_mata*np.cos((PI/1.5)*waktu.get_value()),color=warna_mata, fill_opacity=1).shift(LEFT*0.4 + UP*0.2)))
    mata2.add_updater(lambda z: z.become(Ellipse(width=lebar_mata, height=lebar_mata*np.cos((PI/1.5)*waktu.get_value()),color=warna_mata, fill_opacity=1).shift(RIGHT*0.4 + UP*0.2)))
    self.play(waktu.animate(run_time = 1).set_value(3))
    mata1.clear_updaters()
    mata2.clear_updaters()
    mainpartikel.add_updater(lambda z: z.set_x(0.5*np.sin(time.get_value())))
    alis.add_updater(lambda z: z.set_x(0.5*np.sin(time.get_value())))
    self.add(gelombang)
    self.play(GrowFromCenter(Lens),GrowFromPoint(bell,point_bell),GrowFromPoint(pemukul,point_bell))
    self.play(Rotate(pemukul, rate_func = rush_into,run_time = 0.5 ,angle = -40*DEGREES))
    self.play(bell.animate(run_time = 0.5, rate_func = wiggle).rotate(20*DEGREES),
              AnimationGroup(time.animate.set_value(40*PI),run_time = 3),
              FadeTransform(mainpartikel,alis),
              AnimationGroup(tebal.animate(run_time=1).set_value(0),
                             jari.animate(run_time=1).set_value(4)),
              AnimationGroup(tebal1.animate(run_time=1.5).set_value(0),
                             jari1.animate(run_time=1.5).set_value(3)),
              AnimationGroup(tebal2.animate(run_time=2).set_value(0),
                             jari2.animate(run_time=2).set_value(2)))
    self.wait()