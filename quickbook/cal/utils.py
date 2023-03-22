from datetime import datetime
from calendar import Calendar
from .models import Event


class Day:
    def __init__(self, date: str, weekday: int, events: "Event"):
        self.date: str = date
        self.events: "Event" = events
        self.weekday: int = weekday

    @property
    def day_name(self):
        return [
            "poniedziałek",
            "wtorek",
            "środa",
            "czwartek",
            "piątek",
            "sobota",
            "niedziela",
        ][self.weekday - 1]

class Month:
    def __init__(self, month: int, year: int, weeks: list):
        self.month: int = month
        self.year: int = year
        self.today: str = datetime.now().strftime("%Y-%m-%d")
        self.weeks: list = weeks

    @property
    def month_name(self):
        return [
            'styczeń',
            'luty',
            'marzec',
            'kwiecień',
            'maj',
            'czerwiec',
            'lipiec',
            'sierpień',
            'wrzesień',
            'październik',
            'listopad',
            'grudzień',
        ][self.month - 1]


class QuickBookCalendar(Calendar):
    def __init__(self, year=None, month=None):
        super(QuickBookCalendar, self).__init__()

    def prev_month(self, year, month):
        if month == 1:
            return year - 1, 12
        else:
            return year, month - 1

    def next_month(self, year, month):
        if month == 12:
            return year + 1, 1
        else:
            return year, month + 1

    def monthdays2calendar(self, year: int, month: int) -> list[list[tuple[int, int, int, int]]]:
        days: list = list(self.itermonthdays2(year, month))
        month_weeks: list[list[tuple[int, int, int, int]]] = []

        for i in range(0, len(days), 7):
            week = []
            for x in days[i:i + 7]:
                if x[0] > 0:
                    week.append((x[0], x[1], year, month))
                else:
                    week.append((x[0], x[1], 0, 0))
            month_weeks.append(week)

        return month_weeks

    def monthdays2calendar_trimmed(self, year, month) -> list[list[tuple[int, int, int, int]]]:
        days = list(self.itermonthdays2(year, month))
        month_weeks = []

        for i in range(0, len(days), 7):
            week = []
            for x in days[i:i + 7]:
                if x[0] > 0:
                    week.append((x[0], x[1], year, month))
            month_weeks.append(week)

        return month_weeks

    def week_list(self, theweek: list[tuple[int, int, int, int]], events):
        week = []
        for day, weekday, year, month in theweek:
            y = "{:>04d}".format(year)
            m = "{:>02d}".format(month)
            d = "{:>02d}".format(day)
            week.append(Day(
                date=f"{y}-{m}-{d}",
                weekday=weekday,
                events=events.filter(day__day=day, day__year=year, day__month=month).order_by('start_time')
                )
            )
        return week

    def cal_object(self, year, month):
        prev_month: tuple[int, int] = self.prev_month(year, month)
        next_month: tuple[int, int] = self.next_month(year, month)

        prev_month_days: list[list[tuple[int, int, int, int]]] = self.monthdays2calendar_trimmed(prev_month[0], prev_month[1])
        this_month_days: list[list[tuple[int, int, int, int]]] = self.monthdays2calendar(year, month)
        next_month_days: list[list[tuple[int, int, int, int]]] = self.monthdays2calendar_trimmed(next_month[0], next_month[1])

        events = Event.objects.filter(
            day__range=[
                f"{prev_month[0]}-{prev_month[1]}-20",
                f"{next_month[0]}-{next_month[1]}-10"
            ]
        )

        first_week = this_month_days[0]
        first_week.reverse()
        pivot = -1
        for index, day in enumerate(first_week):
            if day[0] == 0:
                first_week[index] = prev_month_days[-1][pivot]
                pivot -= 1
        first_week.reverse()

        last_week = this_month_days[-1]
        pivot = 0
        for index, day in enumerate(last_week):
            if day[0] == 0:
                last_week[index] = next_month_days[0][pivot]
                pivot += 1

        weeks = []
        for theweek in this_month_days:
            weeks.append(self.week_list(theweek, events))

        return Month(
            month=month,
            year=year,
            weeks=weeks
        )

