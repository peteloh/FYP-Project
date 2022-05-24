"""
Streamlit App to display my results
"""

import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import numpy as np

import pandas as pd

import main

st.set_page_config(layout="wide")
width = st.sidebar.slider("plot width", 1, 50, 25)
height = st.sidebar.slider("plot height", 1, 25, 5)

def linear_regression(df, x, y):
    df = df.sort_values('actual_marks')
    X_train = df[[x]]
    y_train = df[[y]]

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_train)
    intercept = regressor.intercept_
    coef = regressor.coef_
    R2 = regressor.score(X_train, y_train)

    return X_train, y_train, y_pred, R2

def poly_regression(df, x, y):
    df = df.sort_values('actual_marks')
    X_train = df[[x]]
    y_train = df[[y]]

    poly_reg=PolynomialFeatures(degree=2)
    X_poly=poly_reg.fit_transform(X_train)
    poly_reg.fit(X_poly,y_train)
    lin_reg2=LinearRegression()
    lin_reg2.fit(X_poly,y_train)

    y_pred = lin_reg2.predict(poly_reg.fit_transform(X_train))
    R2 = r2_score(y_train, y_pred)
    return X_train, y_train, y_pred, R2

def display_linear_regression(df):
    fig, [ax1, ax2, ax3, ax4, ax5] = plt.subplots(nrows=1, ncols=5, figsize=(width, height))
    line_colour = 'red'
    R2_vals = {}

    X, y, y_pred, R2 = linear_regression(df, x="actual_marks", y="SCOSS_count")
    ax1.scatter(X, y)
    ax1.plot(X, y_pred, color = line_colour)
    ax1.set_ylabel("SCOSS_count (%)")
    ax1.set_xlabel("actual_marks (%)") 
    R2_vals["SCOSS_count"] = round(R2,2)
    
    X, y, y_pred, R2 = linear_regression(df, x="actual_marks", y="SCOSS_set")
    ax2.scatter(X, y)
    ax2.plot(X, y_pred, color = line_colour)
    ax2.set_ylabel("SMOSS_set (%)")
    ax2.set_xlabel("actual_marks (%)") 
    R2_vals["SCOSS_set"] = round(R2,2)

    X, y, y_pred, R2 = linear_regression(df, x="actual_marks", y="SCOSS_hash")
    ax3.scatter(X, y)
    ax3.plot(X, y_pred, color = line_colour)
    ax3.set_ylabel("SCOSS_hash (%)")
    ax3.set_xlabel("actual_marks (%)")
    R2_vals["SCOSS_hash"] = round(R2,2)
    
    X, y, y_pred, R2 = linear_regression(df, x="actual_marks", y="unified_diff")
    ax4.scatter(X, y)
    ax4.plot(X, y_pred, color = line_colour)
    ax4.set_ylabel("unified_diff (%)")
    ax4.set_xlabel("actual_marks (%)")
    R2_vals["unified_diff"] = round(R2,2)

    X, y, y_pred, R2 = linear_regression(df, x="actual_marks", y="tree_diff")
    ax5.scatter(X, y)
    ax5.plot(X, y_pred, color = line_colour)
    ax5.set_ylabel("tree_diff (%)")
    ax5.set_xlabel("actual_marks (%)")
    R2_vals["tree_diff"] = round(R2,2)
    
    st.pyplot(fig)
    return R2_vals

def display_poly_regression(df):
    fig, [ax1, ax2, ax3, ax4, ax5] = plt.subplots(nrows=1, ncols=5, figsize=(width, height))
    line_colour = 'red'
    R2_vals = {}

    X, y, y_pred, R2 = poly_regression(df, x="actual_marks", y="SCOSS_count")
    ax1.scatter(X, y)
    ax1.plot(X, y_pred, color = line_colour)
    ax1.set_ylabel("SCOSS_count (%)")
    ax1.set_xlabel("actual_marks (%)") 
    R2_vals["SCOSS_count"] = round(R2,2)
    
    X, y, y_pred, R2 = poly_regression(df, x="actual_marks", y="SCOSS_set")
    ax2.scatter(X, y)
    ax2.plot(X, y_pred, color = line_colour)
    ax2.set_ylabel("SMOSS_set (%)")
    ax2.set_xlabel("actual_marks (%)") 
    R2_vals["SCOSS_set"] = round(R2,2)

    X, y, y_pred, R2 = poly_regression(df, x="actual_marks", y="SCOSS_hash")
    ax3.scatter(X, y)
    ax3.plot(X, y_pred, color = line_colour)
    ax3.set_ylabel("SCOSS_hash (%)")
    ax3.set_xlabel("actual_marks (%)")
    R2_vals["SCOSS_hash"] = round(R2,2)
    
    X, y, y_pred, R2 = poly_regression(df, x="actual_marks", y="unified_diff")
    ax4.scatter(X, y)
    ax4.plot(X, y_pred, color = line_colour)
    ax4.set_ylabel("unified_diff (%)")
    ax4.set_xlabel("actual_marks (%)")
    R2_vals["unified_diff"] = round(R2,2)

    X, y, y_pred, R2 = poly_regression(df, x="actual_marks", y="tree_diff")
    ax5.scatter(X, y)
    ax5.plot(X, y_pred, color = line_colour)
    ax5.set_ylabel("tree_diff (%)")
    ax5.set_xlabel("actual_marks (%)")
    R2_vals["tree_diff"] = round(R2,2)
    
    st.pyplot(fig)
    return R2_vals

def section1():
    st.title("Code Score Prediction - Training")

    training_data = ["C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15", \
                     "C16", "C17", "C18", "C19", "C20", "C22", "C23", "C24", "C25", "C26", "C27", "C29", "C30"]
    
    st.header("Exercise A")
    df1 = main.analyse("ExA", training_data)
    st.write(df1)
    st.subheader("Linear Regression")
    linear_R2 = display_linear_regression(df1)
    st.subheader("Poly Regression")
    poly_R2 = display_poly_regression(df1)

    col1, col2 = st.columns(2)
    col1.markdown("**Linear Regression $(R^2)$**")
    col1.write(linear_R2)
    col2.markdown("**Poly Regression $(R^2)$**")
    col2.write(poly_R2)

    st.header("Exercise B")
    df2 = main.analyse("ExB", training_data)
    st.write(df2)
    st.subheader("Linear Regression")
    linear_R2 = display_linear_regression(df2)
    st.subheader("Poly Regression")
    poly_R2 = display_poly_regression(df2)

    col1, col2 = st.columns(2)
    col1.markdown("**Linear Regression $(R^2)$**")
    col1.write(linear_R2)
    col2.markdown("**Poly Regression $(R^2)$**")
    col2.write(poly_R2)

    st.header("Exercise C")
    df3 = main.analyse("ExC", training_data)
    st.write(df3)
    st.subheader("Linear Regression")
    linear_R2 = display_linear_regression(df3)
    st.subheader("Poly Regression")
    poly_R2 = display_poly_regression(df3)

    col1, col2 = st.columns(2)
    col1.markdown("**Linear Regression $(R^2)$**")
    col1.write(linear_R2)
    col2.markdown("**Poly Regression $(R^2)$**")
    col2.write(poly_R2)

    st.header("Exercise D")
    df4 = main.analyse("ExD", training_data)
    st.write(df4)
    st.subheader("Linear Regression")
    linear_R2 = display_linear_regression(df4)
    st.subheader("Poly Regression")
    poly_R2 = display_poly_regression(df4)

    col1, col2 = st.columns(2)
    col1.markdown("**Linear Regression $(R^2)$**")
    col1.write(linear_R2)
    col2.markdown("**Poly Regression $(R^2)$**")
    col2.write(poly_R2)

    st.header("All Exercises")
    df_tot = pd.concat([df1, df2, df3, df4])
    st.write(df_tot)
    st.subheader("Linear Regression")
    linear_R2 = display_linear_regression(df_tot)
    st.subheader("Poly Regression")
    poly_R2 = display_poly_regression(df_tot)

    col1, col2 = st.columns(2)
    col1.markdown("**Linear Regression $(R^2)$**")
    col1.write(linear_R2)
    col2.markdown("**Poly Regression $(R^2)$**")
    col2.write(poly_R2)

def predict_marks(df_train, df_test):

    X_train = df_train[["SCOSS_set"]]
    y_train = df_train[["actual_marks"]]

    poly_reg=PolynomialFeatures(degree=2)
    X_poly=poly_reg.fit_transform(X_train)
    poly_reg.fit(X_poly,y_train)
    lin_reg2=LinearRegression()
    lin_reg2.fit(X_poly,y_train)

    y_train_pred = lin_reg2.predict(poly_reg.fit_transform(X_train))
    R2_train = r2_score(y_train, y_train_pred)

    X_test = df_test[["SCOSS_set"]]
    y_test = df_test[["actual_marks"]]

    y_test_pred = lin_reg2.predict(poly_reg.fit_transform(X_test))
    R2_test = r2_score(y_test, y_test_pred)

    # print(df)
    df_results = df_test.drop(columns=["SCOSS_count", "SCOSS_hash", "unified_diff", "tree_diff"])
    df_results = df_results.reset_index(drop=True)

    predicted_marks = np.array(y_test_pred).T.tolist()
    actual_marks = df_results["actual_marks"]
    df_results["predicted_marks"] = y_test_pred
    df_results['accuracy (+-20%)'] = np.where(
        abs(df_results['actual_marks'] - df_results['predicted_marks']) < 0.2, 
        True, 
        False
    )

    subset_df = df_results[df_results["accuracy (+-20%)"] == True]
    accuracy = subset_df.count()
    total = df_results.count()
    accuracy = accuracy["accuracy (+-20%)"]/ total["accuracy (+-20%)"]

    print(accuracy)
    # print(results)
    # df = pd.DataFrame(results)
    # print(df)
    return df_results, accuracy

def section2():
    st.title("Code Score Prediction Testing")
    # chosen model = SCOSS_set, polynomial regression
    training_data = ["C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15", \
                     "C16", "C17", "C18", "C19", "C20", "C22", "C23", "C24", "C25", "C26", "C27", "C29", "C30"]
    testing_data  = ["C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C40"]

    df1_train = main.analyse("ExA", training_data)
    df2_train = main.analyse("ExB", training_data)
    df3_train = main.analyse("ExC", training_data)
    df4_train = main.analyse("ExD", training_data)
    df_train = pd.concat([df1_train, df2_train, df3_train, df4_train])

    df1_test = main.analyse("ExA", testing_data)
    df2_test = main.analyse("ExB", testing_data)
    df3_test = main.analyse("ExC", testing_data)
    df4_test = main.analyse("ExD", testing_data)
    df_test = pd.concat([df1_test, df2_test, df3_test, df4_test])

    results_df, accuracy = predict_marks(df_train, df_test)
    st.write(results_df)
    st.markdown(f"**Accuracy = {round(accuracy*100,0)}%**")
    

# main
section1()
section2()
