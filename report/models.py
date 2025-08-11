from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):
    REPORT_REASON = (
        (0, "Select a reason"),
        (1, "Inappropriate Language"),
        (2, "Hate Speech"),
        (3, "Harassment or Bullying"),
        (4, "Spam or Advertising"),
        (5, "Triggering or Harmful Content"),
        (6, "Other"),
    )

    note = models.ForeignKey('quote.Note', on_delete=models.CASCADE, related_name='reports')
    report_reason = models.IntegerField(default=0)
    reason = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]  # Order by creation date in descending order

    def __str__(self):
        return f"Report for {self.note.content} - Reason: {self.report_reason}"
    
# The Report model is used to track reports made on quotes, including the reason for the report and the associated quote.