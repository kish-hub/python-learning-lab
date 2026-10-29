# AI Dataset Clearance
def main():
    # Ask the user for the source status.
    source_status = input("Enter the source status (Approved or Unverified): ").capitalize().strip()

    # Ask the user for the data state.

    data_state = input("Enter the data state (Anonymized or Identifiable): ").capitalize().strip()

    # Check whether the source status is Approved.
    if source_status == "Approved":
        if data_state == "Anonymized":
            print("Ready for training")
        elif data_state == "Identifiable":
            print("Privacy review required")
        else:
            print("Enter a valid data state")
    # Otherwise, check whether the source status is Unverified.
    elif source_status == "Unverified":
        if data_state == "Anonymized":
            print("Source verification required")
        elif data_state == "Identifiable":
            print("Dataset blocked")
        else:
            print("Enter a valid data state")
    else:
        print("Enter a valid source status")


main()