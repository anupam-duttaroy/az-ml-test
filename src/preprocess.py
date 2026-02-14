from dateutil import parser

def main():
    # 1. Parse Arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--training_data", type=str, help="Path to training data")
    # parser.add_argument("--n_estimators", type=int, default=100)
    # args = parser.parse_args()

    # print(f"Training data path: {args.training_data}")
    # print(f"Number of estimators: {args.n_estimators}")

    dt = parser.parse("2026-02-14 10:30")
    print("Parsed date from pre-processing step:", dt)
    

if __name__ == "__main__":
    main()