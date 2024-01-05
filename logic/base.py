from abc import ABC, abstractmethod
from models.models import db

class BaseLogic(ABC):

    @abstractmethod
    def response(self, request, session):
        """ 各ロジッククラスで実装されるメソッド """
        pass

    @staticmethod
    def manage_transaction(task_func, *args, **kwargs):
        """
        This method is a transaction manager for database operations. 
        It commits on successful execution of the provided task function and rolls back in case of exceptions.

        Args:
            task_func (callable): The function that contains the database operations to be executed.
            *args: Variable list of arguments to be passed to task_func.
            **kwargs: Arbitrary keyword arguments to be passed to task_func.

        Returns:
            Any: The result of task_func, if successful.

        Raises:
            Exception: If task_func raises any exceptions.
        """
        try:
            # Execute the provided task function with the given arguments
            result = task_func(*args, **kwargs)  

            # Commit the changes if task function executed successfully
            db.session.commit()  
            return result

        except Exception as e:
            # Rollback the changes in case of any exceptions during task function execution
            db.session.rollback()  

            # Re-raise the exception for further handling or logging by the caller
            raise e  

        finally:
            # Always close the session after the operations, regardless of success or failure
            db.session.close()  
