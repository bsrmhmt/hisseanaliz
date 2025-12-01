# ai_engine/risk.py
import numpy as np
import pandas as pd

class RiskManager:
    """Portföy risk analizlerini yapan motor"""
    
    def calculate_metrics(self, df):
        """
        Volatilite, VaR ve Max Drawdown hesaplar.
        """
        try:
            # Günlük Yüzdesel Getiriler
            returns = df['Close'].pct_change().dropna()
            
            if len(returns) < 30:
                return None
            
            # 1. Volatilite (Yıllık Risk)
            # Standart sapma * 252 iş günü karekökü
            volatility = returns.std() * np.sqrt(252) * 100
            
            # 2. VaR (Value at Risk - %95)
            # En kötü %5'lik günde ne kadar kaybedersin?
            var_95 = np.percentile(returns, 5) * 100
            
            # 3. Max Drawdown (Zirveden Dibe Düşüş)
            # Tarihi zirvesinden en fazla yüzde kaç düşmüş?
            cumulative = (1 + returns).cumprod()
            peak = cumulative.expanding(min_periods=1).max()
            drawdown = (cumulative / peak) - 1
            max_dd = drawdown.min() * 100
            
            return {
                'volatility': volatility,
                'var_95': var_95,
                'max_drawdown': max_dd,
                'drawdown_series': drawdown # Grafik çizmek için seri
            }
            
        except Exception as e:
            print(f"Risk Hatası: {e}")
            return None
