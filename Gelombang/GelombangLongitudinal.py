config.background_color = '#0f0e17'
class GelombangLongitudinal(MovingCameraScene):
    def construct(self):
        varup = 0.5

        Line1=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line2=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line3=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line4=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line5=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line6=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line7=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line8=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line9=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line10=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line11=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line12=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line13=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line14=Line(start = ORIGIN, end = UP*varup,color=RED)
        Line15=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line16=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line17=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line18=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line19=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line20=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line21=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line22=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line23=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line24=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line25=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line26=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line27=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line28=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line29=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line30=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line31=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line32=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line33=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line34=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line35=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line36=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line37=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line38=Line(start = ORIGIN, end = UP*varup,color=RED)
        Line39=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line40=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line41=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line42=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line43=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line44=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line45=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line46=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line47=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line48=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line49=Line(start = ORIGIN, end = UP*varup,color=BLUE)
        Line50=Line(start = ORIGIN, end = UP*varup,color=BLUE)

        pruh = VGroup(Line1,Line2,Line3,Line4,Line5,Line6,Line7,Line8,Line9,Line10,Line11,Line12,Line13,Line14,Line15,Line16,Line17,Line18,Line19,Line20,Line21,Line22,Line23,Line24,Line25,Line26,Line27,Line28,Line29,Line30,Line31,Line32,Line33,Line34,Line35,Line36,Line37,Line38,Line39,Line40,Line41,Line42,Line43,Line44,Line45,Line46,Line47,Line48,Line49,Line50)

        pruh.set_stroke(width = 2)
        bruh = Axes(x_range=[0, 2*PI], y_range=[-1.5, 1.5, 1])
        plan = NumberPlane()
        
        #self.add(plan)
        self.add(pruh)
        self.camera.frame.scale(0.5).move_to(RIGHT*2.5 + UP*0.25)
        tracker = ValueTracker(0)
        T = 0.5
        A = 0.15
        Line1.add_updater(lambda z: z.set_x(0 + A*np.sin(2*PI*(tracker.get_value()-0)*T)))
        Line2.add_updater(lambda z: z.set_x(0.1 + A*np.sin(2*PI*(tracker.get_value()-0.1)*T)))
        Line3.add_updater(lambda z: z.set_x(0.2 + A*np.sin(2*PI*(tracker.get_value()-0.2)*T)))
        Line4.add_updater(lambda z: z.set_x(0.3 + A*np.sin(2*PI*(tracker.get_value()-0.3)*T)))
        Line5.add_updater(lambda z: z.set_x(0.4 + A*np.sin(2*PI*(tracker.get_value()-0.4)*T)))
        Line6.add_updater(lambda z: z.set_x(0.5 + A*np.sin(2*PI*(tracker.get_value()-0.5)*T)))
        Line7.add_updater(lambda z: z.set_x(0.6 + A*np.sin(2*PI*(tracker.get_value()-0.6)*T)))
        Line8.add_updater(lambda z: z.set_x(0.7 + A*np.sin(2*PI*(tracker.get_value()-0.7)*T)))
        Line9.add_updater(lambda z: z.set_x(0.8 + A*np.sin(2*PI*(tracker.get_value()-0.8)*T)))
        Line10.add_updater(lambda z: z.set_x(0.9 + A*np.sin(2*PI*(tracker.get_value()-0.9)*T)))
        Line11.add_updater(lambda z: z.set_x(1.0 + A*np.sin(2*PI*(tracker.get_value()-1.0)*T)))
        Line12.add_updater(lambda z: z.set_x(1.1 + A*np.sin(2*PI*(tracker.get_value()-1.1)*T)))
        Line13.add_updater(lambda z: z.set_x(1.2 + A*np.sin(2*PI*(tracker.get_value()-1.2)*T)))
        Line14.add_updater(lambda z: z.set_x(1.3 + A*np.sin(2*PI*(tracker.get_value()-1.3)*T)))
        Line15.add_updater(lambda z: z.set_x(1.4 + A*np.sin(2*PI*(tracker.get_value()-1.4)*T)))
        Line16.add_updater(lambda z: z.set_x(1.5 + A*np.sin(2*PI*(tracker.get_value()-1.5)*T)))
        Line17.add_updater(lambda z: z.set_x(1.6 + A*np.sin(2*PI*(tracker.get_value()-1.6)*T)))
        Line18.add_updater(lambda z: z.set_x(1.7 + A*np.sin(2*PI*(tracker.get_value()-1.7)*T)))
        Line19.add_updater(lambda z: z.set_x(1.8 + A*np.sin(2*PI*(tracker.get_value()-1.8)*T)))
        Line20.add_updater(lambda z: z.set_x(1.9 + A*np.sin(2*PI*(tracker.get_value()-1.9)*T)))
        Line21.add_updater(lambda z: z.set_x(2.0 + A*np.sin(2*PI*(tracker.get_value()-2.0)*T)))
        Line22.add_updater(lambda z: z.set_x(2.1 + A*np.sin(2*PI*(tracker.get_value()-2.1)*T)))
        Line23.add_updater(lambda z: z.set_x(2.2 + A*np.sin(2*PI*(tracker.get_value()-2.2)*T)))
        Line24.add_updater(lambda z: z.set_x(2.3 + A*np.sin(2*PI*(tracker.get_value()-2.3)*T)))
        Line25.add_updater(lambda z: z.set_x(2.4 + A*np.sin(2*PI*(tracker.get_value()-2.4)*T)))
        Line26.add_updater(lambda z: z.set_x(2.5 + A*np.sin(2*PI*(tracker.get_value()-2.5)*T)))
        Line27.add_updater(lambda z: z.set_x(2.6 + A*np.sin(2*PI*(tracker.get_value()-2.6)*T)))
        Line28.add_updater(lambda z: z.set_x(2.7 + A*np.sin(2*PI*(tracker.get_value()-2.7)*T)))
        Line29.add_updater(lambda z: z.set_x(2.8 + A*np.sin(2*PI*(tracker.get_value()-2.8)*T)))
        Line30.add_updater(lambda z: z.set_x(2.9 + A*np.sin(2*PI*(tracker.get_value()-2.9)*T)))
        Line31.add_updater(lambda z: z.set_x(3.0 + A*np.sin(2*PI*(tracker.get_value()-3.0)*T)))
        Line32.add_updater(lambda z: z.set_x(3.1 + A*np.sin(2*PI*(tracker.get_value()-3.1)*T)))
        Line33.add_updater(lambda z: z.set_x(3.2 + A*np.sin(2*PI*(tracker.get_value()-3.2)*T)))
        Line34.add_updater(lambda z: z.set_x(3.3 + A*np.sin(2*PI*(tracker.get_value()-3.3)*T)))
        Line35.add_updater(lambda z: z.set_x(3.4 + A*np.sin(2*PI*(tracker.get_value()-3.4)*T)))
        Line36.add_updater(lambda z: z.set_x(3.5 + A*np.sin(2*PI*(tracker.get_value()-3.5)*T)))
        Line37.add_updater(lambda z: z.set_x(3.6 + A*np.sin(2*PI*(tracker.get_value()-3.6)*T)))
        Line38.add_updater(lambda z: z.set_x(3.7 + A*np.sin(2*PI*(tracker.get_value()-3.7)*T)))
        Line39.add_updater(lambda z: z.set_x(3.8 + A*np.sin(2*PI*(tracker.get_value()-3.8)*T)))
        Line40.add_updater(lambda z: z.set_x(3.9 + A*np.sin(2*PI*(tracker.get_value()-3.9)*T)))
        Line41.add_updater(lambda z: z.set_x(4.0 + A*np.sin(2*PI*(tracker.get_value()-4.0)*T)))
        Line42.add_updater(lambda z: z.set_x(4.1 + A*np.sin(2*PI*(tracker.get_value()-4.1)*T)))
        Line43.add_updater(lambda z: z.set_x(4.2 + A*np.sin(2*PI*(tracker.get_value()-4.2)*T)))
        Line44.add_updater(lambda z: z.set_x(4.3 + A*np.sin(2*PI*(tracker.get_value()-4.3)*T)))
        Line45.add_updater(lambda z: z.set_x(4.4 + A*np.sin(2*PI*(tracker.get_value()-4.4)*T)))
        Line46.add_updater(lambda z: z.set_x(4.5 + A*np.sin(2*PI*(tracker.get_value()-4.5)*T)))
        Line47.add_updater(lambda z: z.set_x(4.6 + A*np.sin(2*PI*(tracker.get_value()-4.6)*T)))
        Line48.add_updater(lambda z: z.set_x(4.7 + A*np.sin(2*PI*(tracker.get_value()-4.7)*T)))
        Line49.add_updater(lambda z: z.set_x(4.8 + A*np.sin(2*PI*(tracker.get_value()-4.8)*T)))
        Line50.add_updater(lambda z: z.set_x(4.9 + A*np.sin(2*PI*(tracker.get_value()-4.9)*T)))

        self.play(tracker.animate(run_time=30,rate_func=linear).set_value(50))
        
