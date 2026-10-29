# AI Dataset Clearance
def main():
    # Ask the user for the source status.
    source_status = input("Enter the source status (Approved or Unverified): ").strip().capitalize()

    # Ask the user for the data state.

    data_state = input("Enter the data state (Anonymized or Identifiable): ").strip().capitalize()
    # Check whether the source status is Approved.
    if not (source_status == "Approved" or source_status == "Unverified"):
        print("Enter a valid source status")
        return
    
    if not (data_state == "Anonymized" or data_state == "Identifiable"):
        print("Enter a valid data state")
        return

    # Check the source status and data state to determine the next steps.
    if source_status == "Approved" and data_state == "Anonymized":
        print("Ready for training")
    elif source_status == "Unverified" and data_state == "Identifiable":
        print("Privacy review required")
    elif source_status == "Unverified" and data_state == "Anonymized":
        print("Source verification required")
    else:
        print("Dataset blocked")

main()