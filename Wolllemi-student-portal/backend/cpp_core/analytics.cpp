#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

namespace py = pybind11;

struct GradeStats {
    double average;
    double median;
    double standard_deviation;
    double trend_slope;
};

GradeStats calculate_analytics(const std::vector<int>& scores) {
    if (scores.empty()) return {0.0, 0.0, 0.0, 0.0};

    double sum = std::accumulate(scores.begin(), scores.end(), 0.0);
    double avg = sum / scores.size();

    std::vector<int> sorted_scores = scores;
    std::sort(sorted_scores.begin(), sorted_scores.end());
    double median = (sorted_scores.size() % 2 == 0) 
        ? (sorted_scores[sorted_scores.size()/2 - 1] + sorted_scores[sorted_scores.size()/2]) / 2.0 
        : sorted_scores[sorted_scores.size()/2];

    double sq_sum = std::inner_product(scores.begin(), scores.end(), scores.begin(), 0.0);
    double stdev = std::sqrt(sq_sum / scores.size() - avg * avg);

    // Simple Linear Regression for Trend (Slope)
    double x_sum = 0, y_sum = sum, xy_sum = 0, x2_sum = 0;
    int n = scores.size();
    for (int i = 0; i < n; ++i) {
        x_sum += i;
        xy_sum += i * scores[i];
        x2_sum += i * i;
    }
    double slope = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum * x_sum);

    return {avg, median, stdev, slope};
}

PYBIND11_MODULE(analytics_engine, m) {
    py::class_<GradeStats>(m, "GradeStats")
        .def_readwrite("average", &GradeStats::average)
        .def_readwrite("median", &GradeStats::median)
        .def_readwrite("standard_deviation", &GradeStats::standard_deviation)
        .def_readwrite("trend_slope", &GradeStats::trend_slope);

    m.def("calculate_analytics", &calculate_analytics, "A function that calculates grade analytics using C++");
}
