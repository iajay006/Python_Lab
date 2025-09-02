class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Add two Time objects
    def add_time(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    # Convert Time object to total seconds
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # Convert seconds back into Time object
    @classmethod
    def from_seconds(cls, total_seconds):
        total_seconds = total_seconds % (24 * 3600)  # wrap around 24 hours
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    # Print time in readable format
    def print_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")


# Example usage
# Current time
current_time = Time(14, 30, 0)   # 2:30:00 PM

# Bread maker takes 3 hours 45 minutes
bread_time = Time(3, 45, 0)

# When will bread be ready?
done_time = current_time.add_time(bread_time)

print("Current Time: ", end="")
current_time.print_time()

print("Bread Time:   ", end="")
bread_time.print_time()

print("Done Time:    ", end="")
done_time.print_time()
