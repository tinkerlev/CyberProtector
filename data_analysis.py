import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def load_login_attempts(db_path):
    """Load login attempts data from the database."""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM login_attempts", conn)
    conn.close()
    return df


def analyze_login_attempts(df):
    print("Basic Statistics:")
    print(df.describe())

    # Additional data analysis
    df['attempt_time'] = pd.to_datetime(df['attempt_time'])
    df.set_index('attempt_time', inplace=True)
    login_attempts_by_hour = df.resample('H').count()

    print("Login attempts by hour:")
    print(login_attempts_by_hour)

    # Check if the DataFrame is not empty before drawing the graph
    if not login_attempts_by_hour.empty:
        login_attempts_by_hour.plot(kind='bar')
        plt.title('Login Attempts by Hour')
        plt.xlabel('Hour')
        plt.ylabel('Number of Attempts')
        plt.show()
    else:
        print("No drawing data available.")


def plot_login_attempts(login_attempts_by_hour):
    """Plot login attempts data."""
    login_attempts_by_hour.plot(kind='bar')
    plt.title('Login Attempts by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Number of Attempts')
    plt.show()


def main(db_path='cyberprotector.db'):
    df = load_login_attempts(db_path)
    login_attempts_by_hour = analyze_login_attempts(df)
    plot_login_attempts(login_attempts_by_hour)


if __name__ == "__main__":
    main()
