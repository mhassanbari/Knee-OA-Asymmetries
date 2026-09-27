import pandas as pd
import numpy as np
from scipy import stats
from 01_data_preprocessing import calculate_asymmetry_index

def analyze_load_asymmetry(df):
    """
    Performs statistical comparison of load asymmetry between non-fatigued 
    and fatigued conditions.
    """
    # Calculate asymmetry indices (%)
    df['asymmetry_non_fatigued'] = calculate_asymmetry_index(
        df['peak_vgrf_affected_nf'], df['peak_vgrf_unaffected_nf']
    )
    df['asymmetry_fatigued'] = calculate_asymmetry_index(
        df['peak_vgrf_affected_f'], df['peak_vgrf_unaffected_f']
    )
    
    # Paired t-test
    t_stat, p_val = stats.ttest_rel(df['asymmetry_fatigued'], df['asymmetry_non_fatigued'])
    
    mean_nf = df['asymmetry_non_fatigued'].mean()
    sd_nf = df['asymmetry_non_fatigued'].std()
    mean_f = df['asymmetry_fatigued'].mean()
    sd_f = df['asymmetry_fatigued'].std()
    
    diff = df['asymmetry_fatigued'] - df['asymmetry_non_fatigued']
    mean_diff = diff.mean()
    sd_diff = diff.std()
    
    # Cohen's d
    cohen_d = mean_diff / sd_diff
    
    print(f"Non-Fatigued Asymmetry: {mean_nf:.1f} ± {sd_nf:.1f}%")
    print(f"Fatigued Asymmetry: {mean_f:.1f} ± {sd_f:.1f}%")
    print(f"Mean Difference: {mean_diff:.1f} ± {sd_diff:.1f}% (t = {t_stat:.2f}, p = {p_val:.3e}, Cohen's d = {cohen_d:.2f})")
    
    return df

def analyze_task_differences(df_tasks):
    """
    One-way ANOVA across tasks (Level Walking, Sit-to-Stand, Stair Negotiation).
    """
    tasks = ['walking', 'sit_to_stand', 'stair_negotiation']
    task_groups = [df_tasks[df_tasks['task'] == task]['asymmetry_increase'] for task in tasks]
    
    f_stat, p_val = stats.f_oneway(*task_groups)
    print(f"\nTask-Specific ANOVA: F = {f_stat:.2f}, p = {p_val:.3e}")

if __name__ == "__main__":
    # Example placeholder execution structure
    pass