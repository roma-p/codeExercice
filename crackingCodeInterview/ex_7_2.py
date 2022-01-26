import logging

logging.basicConfig()
log = logging.getLogger("GearCreator")
log.setLevel(logging.DEBUG)


class CallCenter():

    def __init__(self):
        self.respondents = set()
        self.managers = set()
        self.director = None
        self.call_historic = set()

    def addManagers(self, *managers):
        for manager in managers:
            self.managers.add(manager)

    def addRespondents(self, *respondents):
        for respondent in respondents:
            self.respondents.add(respondent)

    def createTeam(self, manager, *respondents):
        status = True
        if manager not in self.managers:
            log.error("{} not found in call center's managers".format(
                manager.name))
            status = False
        unknown_respondents = set(respondents) - self.respondents
        if unknown_respondents:
            log.error("{} not found in call center's respondents".format(
                unknown_respondents))
            status = False
        if status:
            for respondent in respondents:
                respondent.changeManager(manager)
        return status

    def dispatchCall(self, call):
        for respondent in self.respondents:
            if respondent.takeCall(call):
                return True
        for manager in self.managers:
            if manager.takeCall(call):
                return True
        if self.director.takeCall(call):
            return True
        return False

    def dispatchNewCall(self):
        call = Call()
        self.call_historic.add(call)
        return self.dispatchCall(call)

    def dispatchUnHandledCall(self):
        unhandled = set()
        for call in (call for call in self.call_historic if call.status == 0):
            if not self.dispatchCall(call):
                unhandled.add(call)
        if not unhandled:
            return True
        else:
            log.warning("following calls are still not hundled:")
            for call in unhandled:
                log.warning(call)
            return False


class Personn():

    def __init__(self, name):
        self.name = name
        self.currentCall = None

    def takeCall(self, call):
        if self.currentCall:
            return False
        if call.takeCall(self):
            self.currentCall = call
            log.info("{} taken by {}".format(str(call), self.name))
            return True
        else:
            log.error("call {} already taken".format(str(call)))
            return False

    def closeCall(self):
        if self.currentCall:
            self.currentCall.close()
            self.currentCall = None
            log.info("{} closed by {}".format(
                str(self.currentCall),
                self.name))
            return True
        else:
            return False

    def transferCall(self, call):
        raise NotImplementedError()


class Respondents(Personn):

    def __init__(self, name, manager=None):
        super().__init__(name)
        self.manager = manager

    def transferCall(self, call):
        return self.manager.takeCall(call)

    def changeManager(self, newManager):
        if self.manager:
            self.manager.respondents.pop(self)
        self.manager = newManager
        print(self.manager.name)
        self.manager.respondents.add(self)

class Manager(Personn):

    def __init__(self, name, director=None):
        super().__init__(name)
        self.director = director
        self.respondents = set()

    def transferCall(self, call):
        return self.director.takeCall(call)


class Director(Personn):

    def __init__(self, name):
        super().__init__(name)
        self.managers = set()

    def transferCall(self, call):
        return False


class Call():
    call_idx = 0

    def __init__(self):
        self.call_id = self.genCallId()
        self.status = 0  # 0 -> to take, 1-> taken, 2-> closed.
        self.historic = []

    def __str__(self):
        return self.call_id

    def genCallId(cls):
        cls.call_idx += 1
        return 'call_' + str(cls.call_idx)

    def takeCall(self, personn):
        if not self.status:
            self.status = 1
            return True
        else:
            return False
        self.historic.append(personn)

    def closeCall(self):
        if self.status == 1:
            self.status == 2
            return True
        else:
            return False

