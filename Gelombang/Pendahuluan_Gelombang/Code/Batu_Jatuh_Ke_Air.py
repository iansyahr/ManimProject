from manim import *

#use transparent mode for this code
#3d btw
class Batu_Jatuh_Ke_Air(ThreeDScene):
  def construct(self):
    tebal = ValueTracker(30)
    jari = ValueTracker(0.15)
    tebal1 = ValueTracker(30)
    jari1 = ValueTracker(0.15)
    tebal2 = ValueTracker(30)
    jari2 = ValueTracker(0.15)
    jelas = ValueTracker(0)

    d = -0.48
    p = -0.7
    f = 2.5
    s = 6
    A = 1

    batu = Dot3D(radius=0.25).set_color(GREY)
    gerak_partikel = ValueTracker(15)
    opasitas = ValueTracker(0)
    batu.add_updater(lambda z : z.become(Dot3D(radius=0.25).shift(UP*gerak_partikel.get_value()).set_color(GREY).set_opacity(-(A/(abs(s)**(s*np.sin(f*opasitas.get_value()-p)-d*s) + 1)-1))))

    a1 = Circle(radius=0.15,stroke_width = 30).set_color(WHITE).set_stroke(opacity = 0)
    a2 = Circle(radius=0.15,stroke_width = 30).set_color(WHITE).set_stroke(opacity = 0)
    a3 = Circle(radius=0.15,stroke_width = 30).set_color(WHITE).set_stroke(opacity = 0)

    a1.add_updater(lambda z: z.become(Circle(radius=jari.get_value() ,stroke_width = tebal.get_value()).set_color(WHITE).set_stroke(opacity = jelas.get_value())))
    a2.add_updater(lambda z: z.become(Circle(radius=jari1.get_value() ,stroke_width = tebal1.get_value()).set_color(WHITE).set_stroke(opacity = jelas.get_value())))
    a3.add_updater(lambda z: z.become(Circle(radius=jari2.get_value() ,stroke_width = tebal2.get_value()).set_color(WHITE).set_stroke(opacity = jelas.get_value())))

    air = VGroup(a1,a2,a3)

    self.set_camera_orientation(phi=70 * DEGREES, theta=-90 * DEGREES,focal_distance=80)
    #self.add(ThreeDAxes())
    self.add(batu)
    #focal_distance=80
    self.add(air)
    self.play(AnimationGroup(AnimationGroup(gerak_partikel.animate.set_value(-3),opasitas.animate.set_value(1.5),run_time = 2, rate_func = linear),
                             AnimationGroup(AnimationGroup(tebal.animate(run_time=1).set_value(0),jari.animate(run_time=1).set_value(4),jelas.animate(run_time = 0.3).set_value(1)),
                                            AnimationGroup(tebal1.animate(run_time=1.5).set_value(0),jari1.animate(run_time=1.5).set_value(3),jelas.animate(run_time = 0.3).set_value(1)),
                                            AnimationGroup(tebal2.animate(run_time=2).set_value(0),jari2.animate(run_time=2).set_value(2),jelas.animate(run_time = 0.3).set_value(1))),lag_ratio =0.6))
    self.wait(2)
