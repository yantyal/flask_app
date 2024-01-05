from flask import current_app, render_template

class Validator:
    
    @staticmethod
    def is_user_logged_in(session):
        """
        Check if the user is logged in based on the session.
        
        Parameters:
        - session: The session object (typically from Flask)
        
        Returns:
        - bool: True if the user is logged in, False otherwise
        """
        user_id = session.get('user_id')
        # ログを出力
        current_app.logger.info(f"セッションチェック。UserId: {user_id}") 
        return bool(user_id)
    
    @staticmethod
    def redirect(session):
        if not Validator.is_user_logged_in(session):
            return render_template('login.html')
