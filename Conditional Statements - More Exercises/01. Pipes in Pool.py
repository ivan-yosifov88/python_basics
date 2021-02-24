volume_of_pool = int(input())
pipe_1_flow = int(input())
pipe_2_flow = int(input())
hours = float(input())
total_pipe_flow = pipe_1_flow + pipe_2_flow
percent_fill_of_the_pool = total_pipe_flow * hours / volume_of_pool * 100
pipe_1_flow_in_percent = pipe_1_flow / total_pipe_flow * 100
pipe_2_flow_in_percent = pipe_2_flow / total_pipe_flow * 100
fill_volume = (pipe_1_flow + pipe_2_flow) * hours
difference = abs(volume_of_pool - fill_volume)
if fill_volume <= volume_of_pool:
    print(f"The pool is {percent_fill_of_the_pool:.2f}% full. Pipe 1: {pipe_1_flow_in_percent:.2f}%. Pipe 2: {pipe_2_flow_in_percent:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {difference} liters.")

