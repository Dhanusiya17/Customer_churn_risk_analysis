from pydantic import BaseModel
from typing import List


class CustomerRiskProfile(BaseModel):
    customer_id: str
    churn_flag: int
    tenure_months: int
    usage_intensity_score: float
    monthly_charges: float
    support_tickets_count: int
    escalations: int


class AggregateMetric(BaseModel):
    metric_name: str
    metric_value: float


class QueryResult(BaseModel):
    rows: List[dict]
