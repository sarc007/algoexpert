"""
Write a function that takes in a list of numbers and returns a dictionary containing the following statistics
about the numbers: the mean, median, mode, sample variance, sample standard deviation,
and 95% confidence interval for the mean.
Note that:
•	You can assume that the given list contains a large-enough number of samples from a population to use a
    z-score of 1.96.
•	If there's more than one mode, your function can return any of them.
•	You shouldn't use any libraries.
•	Your output values will automatically be rounded to the fourth decimal.

Sample Input
input.list = [2, 1, 3, 4, 4, 5, 6, 7]
Sample Output
{
"mean": 4.0,
"median": 4.0,
"mode": 4.0,
"sample_variance": 4.0, "sample_standard_deviation": 2.0,
"mean_confidenceinterval": [2.6141, 5.3859],
}



"""


def get_statistics(input_list):
    # Write your code here.

    if len(input_list) == 0:
        return {
            "mean": 0,
            "median": 0,
            "mode": 0,
            "sample_variance": 0,
            "sample_standard_deviation": 0,
            "mean_confidence_interval": [0, 0],
        }

    input_list.sort()
    z_score = 1.96
    mean = sum(input_list) / len(input_list)

    if (len(input_list) % 2) == 0:
        median = (input_list[int((len(input_list) / 2))] + input_list[int((len(input_list) / 2) - 1)]) / 2
    else:
        median = input_list[int((len(input_list) - 1) / 2)]

    frequency_count = {}
    i = 0
    for element in input_list:
        if element in frequency_count:
            frequency_count[element] += 1
        else:
            frequency_count[element] = 1
    mode = min(input_list)
    mode_value = 0
    for element in frequency_count:
        if frequency_count.get(element) > mode_value:
            mode_value = frequency_count.get(element)
            mode = element

    sample_variance = 0.0
    sample_standard_deviation = 0.0
    mean_confidence_interval = []

    for element in input_list:
        sample_variance = sample_variance + ((element - mean) ** 2)
    sample_variance = sample_variance / (len(input_list) - 1)

    sample_standard_deviation = (sample_variance) ** 0.5
    sample_error = z_score * (sample_standard_deviation / (len(input_list) ** 0.5))
    mean_confidence_interval.append(mean - sample_error)
    mean_confidence_interval.append(mean + sample_error)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }

