import logging
from shape_manager import ShapeManager
import rectangle
import square
import circle

logging.basicConfig(level=logging.INFO,
                    format= "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
                    handlers= [
                        logging.FileHandler("app.log", encoding="utf-8")
                    ]
                )

logger = logging.getLogger(__name__)


def main():
    """Execute the main program logic and log execution."""
    logger.info("The program started running")
    manager = ShapeManager()

    while True:

        print("\n--- Shape Management System ---")
        print("1. Add shape")
        print("2. Show all shapes")
        print("3. Update shape")
        print("4. Delete shape")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")


        if choice == '1':
            logger.info("add shape chosen")
            print("\nChoose a shape:")
            print("1. Square")
            print("2. Rectangle")
            print("3. Circle")
            shape_choice = input("Enter shape type (1-3): ")

            try:
                shape_id = manager.get_new_id()

                if shape_choice == '1':
                    side = float(input("Enter side length: "))
                    shape_dic = {"id": shape_id, "shape_type": "square", "side": side}

                elif shape_choice == '2':
                    width = float(input("Enter width: "))
                    height = float(input("Enter height: "))
                    shape_dic = {"id": shape_id, "shape_type": "rectangle", "width": width, "height": height}

                elif shape_choice == '3':
                    radius = float(input("Enter radius: "))
                    shape_dic = {"id": shape_id, "shape_type": "circle", "radius": radius}

                else:
                    print("Invalid choice. Returning to main menu.")
                    continue

                created_shape = manager.create_shape(shape_dic)
                if created_shape:
                    print("Shape added successfully!")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == '2':
            logger.info("Show all shapes chosen")
            print("\n--- All Shapes ---")

            shapes = manager.get_all_shapes()

            if not shapes:
                print("No shapes found in the system.")
            else:
                print("Current Shapes in System:")
                for shape in shapes:
                    print(shape.to_dict())
                    print(f"Area: {shape.get_area():.2f}")
                    print(f"Perimeter: {shape.get_perimeter():.2f}")
                    print("-----------------")


        elif choice == '3':
            logger.info("update shape chosen")
            try:
                shape_id = int(input("Enter the ID of the shape to update: "))
                target_shape = None
                for shape in manager.get_all_shapes():
                    if shape.id == shape_id:
                        target_shape = shape
                        break

                if target_shape is None:
                    print(f"Update failed. Shape with ID {shape_id} does not exist.")
                    continue

                new_data = {}
                print(f"Found shape of type: {target_shape.shape_type}")

                if target_shape.shape_type == "square":
                    new_data["side"] = float(input("Enter new side length: "))

                elif target_shape.shape_type == "rectangle":
                    new_data["width"] = float(input("Enter new width: "))
                    new_data["height"] = float(input("Enter new height: "))

                elif target_shape.shape_type == "circle":
                    new_data["radius"] = float(input("Enter new radius: "))

                if manager.update_shape(shape_id, new_data):
                    print(f"Shape with ID {shape_id} updated successfully.")
                else:
                    print(f"Update failed. Shape with ID {shape_id} does not exist.")

            except ValueError:
                print("Invalid ID! Please enter a number.")

        elif choice == '4':
            logger.info("delete shape chosen")
            try:
                shape_id = int(input("Enter the ID of the shape to delete: "))
                if manager.delete_shape(shape_id):
                    print(f"Shape with ID {shape_id} deleted successfully.")
                else:
                    print(f"Delete failed. Shape with ID {shape_id} does not exist.")
            except ValueError:
                print("Invalid ID! Please enter a number.")

        elif choice == '5':
            logger.info("The program was closed by the user.")
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()