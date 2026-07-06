"""
EVGuard — Prediction Response Schema
=====================================
Pydantic v2 models for the POST /api/v1/predict response body.
"""

from pydantic import BaseModel, Field
from typing import Optional


class FeatureContribution(BaseModel):
    """One feature's contribution to the prediction."""
    feature: str
    display_name: str
    value: float
    importance: float
    status: str = Field(description="normal | warning | critical")
    normal_range: list[float]


class Recommendation(BaseModel):
    """One actionable recommendation based on the prediction."""
    severity: str = Field(description="INFO | WARNING | CRITICAL")
    component: str
    message: str
    action: str


class PredictionResponse(BaseModel):
    """Full prediction response including class, probabilities, risk, and recommendations."""
    predicted_class: str
    predicted_label: int
    probabilities: dict[str, float]
    risk_level: str
    confidence: float
    feature_contributions: list[FeatureContribution]
    recommendations: list[Recommendation]
    model_version: str
    prediction_id: str
    timestamp: str
