from datetime import datetime
import uuid


class IntakeAgent:

    def process(self, application):

        return {
            "application_id": str(uuid.uuid4())[:8],
            "timestamp": datetime.now().isoformat(),
            "application": application
        }