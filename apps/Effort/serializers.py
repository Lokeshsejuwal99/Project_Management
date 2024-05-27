from apps.Effort.models import EffortCalculation
from rest_framework import serializers
import pytz
from datetime import datetime, timedelta, timezone


class EffortCalculateSerializer(serializers.ModelSerializer):
    """Serializer for EffortCalculation"""

    remind = serializers.CharField(read_only=True)

    class Meta:
        model = EffortCalculation
        fields = ["task", "project", "start_time", "end_time", "notes", "remind"]
        # fields = '__all__'

        def to_representation(self, instance):
            """Convert model objects to dictionery representation"""
            representation = super().to_representation(instance)
            kathmandu_tz = pytz.timezone("Asia/Kathmandu")
            current_time = datetime.now(timezone.utc)
            converted_timezone = current_time.astimezone(kathmandu_tz)
            current_time_str = converted_timezone.strftime("%Y-%m-%d %H:%M:%S%z")
            current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S%z")

            # Start/End time
            start_time = instance.start_time
            end_time = instance.end_time
            print("Start_time", start_time)
            print("Current_time", current_time)
            print("End_time", end_time)

            if current_time > end_time:
                representation["status"] = "Finished"
                representation["remind"] = "Task/Project already finished"
            else:
                if current_time > start_time:
                    duration_seconds = (end_time - current_time).total_seconds()
                else:
                    duration_seconds = (end_time - start_time).total_seconds()

                days, remainder = divmod(duration_seconds, 86400)
                hours, remainder = divmod(remainder, 3600)
                minutes, seconds = divmod(remainder, 60)

                if duration_seconds < 3600:
                    if minutes == 0:
                        representation["remind"] = f"{int(seconds)} seconds left."
                    else:
                        representation["remind"] = f"{int(minutes)} minutes {int(seconds)} seconds left."
                elif duration_seconds >= 3600 and duration_seconds <= 86400:
                    representation["remind"] = f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds left."
                else:
                    representation["remind"] = f"{int(days)} days, and {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds left."
                    representation["remind"] = "On progress.."
            return representation
