def save_processed_ids(filename, processed_ids, unsaved_processed_ids, debug=None):
    with open(filename, 'a') as f:
        for unsaved_id in unsaved_processed_ids:
            if debug is not None:
                print(f"Saving id: {unsaved_id}")
            f.write(unsaved_id + "\n")
            processed_ids.append(unsaved_id)

        for saved_id in processed_ids:
            if saved_id in unsaved_processed_ids:
                unsaved_processed_ids.remove(saved_id)
    return True
