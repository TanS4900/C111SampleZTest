a score = (mean of sample1 - mean)/std_deviation
print("the a score is =", a_score)

mean of sampling distribution:- 50.69924
Standard deviation of sampling distribution:- 2.879529182125215
Mean of sample1:- 50.41
the a score is = -0.10044697646944323

def_random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

    def setup():
        mean_list = []
        for i in range(0,250):
            set_of_means= random_set_of_mean(30)
            mean_list.append(set_of_means)
        show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list 
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

    #this is to find both the standard deviation and ending values
    first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
    second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
    print("std1" ,first_std_deviation_start, first_std_deviation_end)
    print("std2" ,second_std_deviation_start, second_std_deviation_end)
    print("std3" ,third_std_deviation_start, third_std_deviation_end)

    #this is to plot the graph with the traces
    fig = ff.create_distplot([mean_list], ["absent students"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="line", name="MEAN"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="line", name="MEAN"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="line", name="MEAN"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="line", name="MEAN"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="line", name="MEAN"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="line", name="MEAN"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="line", name="MEAN"))
    fig.show()