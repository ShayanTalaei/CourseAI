class TimePeriod:

    def __init__(self, todo, section, start_time, end_time):
        self.todo = todo
        self.section = section
        self.start_time = start_time
        self.end_time = end_time

class Plan:

    def __init__(self, time_periods):
        self.time_periods = time_periods

    def choose_critical_sections(sections, weights, k=3):
        chosen_sections, chosen_weights = [], []
        for i in range(k):
            max_weight, max_index = 0, 0
            if len(weights) == 0:
                break
            for j, weight in enumerate(weights):
                if weight > max_weight:
                    max_index = j
                    max_weight = weight
            chosen_sections.append(sections.pop(j))
            chosen_weights.append(weights.pop(j))
        return chosen_sections, chosen_weights

    def generate_plan(sections, weights, start_time=13, end_time=19):
        sections, weights = Plan.choose_critical_sections(sections, weights)
        sum_weights = sum(weights)*1.15
        last_time = start_time
        total_time = last_time - start_time
        total_rest_time = (0.15 / 1.15) * total_time
        unit_rest_time = total_rest_time / len(weights)
        time_periods = []
        for section, weight in zip(sections, weights):
            study_time = int((weight / sum_weights) * total_time / 3)
            test_time = int((weight / sum_weights) * total_time *2 / 3)
            study_period = TimePeriod("Study", section, last_time, last_time + study_time)
            test_period = TimePeriod("Test", section, last_time + study_time, last_time + study_time + test_time)
            rest_period = TimePeriod("Rest", section, last_time + study_time + test_time,
                                         last_time + study_time + test_time + unit_rest_time)
            last_time += study_time + test_time + unit_rest_time
            time_periods += [study_period, test_period, rest_period]
        return Plan(time_periods)
        
    def summary_text(self):
        total_study_time, total_test_time, total_time = 0, 0, 0
        sections = []
        for time_period in self.time_periods:
            if time_period.todo == "Study":
                total_study_time += time_period.end_time - time_period.start_time
                sections.append(time_period.section)
            if time_period.todo == "Test":
                total_test_time += time_period.end_time - time_period.start_time

        total_time = self.time_periods[-1].end_time - self.time_periods[0].start_time
        
        summary = "تست بزنیم." + str(total_test_time) + "ساعت درس بخونی و " + str(total_study_time) + "ساعت کار کنیم. قراره مجموعا " + str(total_time) + "رو برای " + "، ".join(sections) + "الان میخوایم مباحث "
        return summary