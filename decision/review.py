def climb_ladder(step_remaining, steps_crossed):
  if(steps_remaining > steps_crossed):
    print("Still some ways to go")
  else:
    print("We are almost there")
climb_ladder(5, 2)
climb_ladder(2, 5)
