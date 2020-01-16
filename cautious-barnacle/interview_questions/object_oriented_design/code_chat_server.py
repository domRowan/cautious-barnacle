from datetime import datetime
from sets import Set
import heapq
import uuid


class ConversationManager:
    def __init__(self):
        self.conversationToCustomers = {}

    def hasAcceptedConversation(self, customer, conversation):
        return customer in self.conversationToCustomers[conversation.id]

    def acceptConversation(self, customer, conversation):

        if not self.conversationToCustomers[conversation.id]:
            self.conversationToCustomers[conversation.id] = Set([])

        self.conversationToCustomers[conversation.id].add(customer.id)

    def rejectConversation(self, customer, conversation):
        raise NotImplementedError


class Customer:
    def __init__(self):
        self.id = uuid.uuid4()  # generate unique ID using uuid
        self.available = False
        self.contactToConversation = {}
        self.groupToConversations = {}

    def setAvailability(self, value):
        self.available = value

    def createConversation(self, customers):
        conversation = Converastion(customers)
        if (len(customers) > 1):
            self.groupToConversations[conversation.id] = conversation
        else:
            self.contactToConversation[customers[0].id] = conversation

    def getConversation(self, customer):
        return self.contactToConversation[customer.id]

    def sendMessage(self, customer, message):
        if not self.contactToConversation[customer.id]:
            self.createConversation(customer)

        conversation = self.getConversation(customer)

        conversation.addMessage(message)


class Converastion:
    def __init__(self, customers):
        self.id = uuid.uuid4()
        self.customers = customers
        self.acceptedCustomers = []
        self.messages = []

    def addCustomer(self, customer):
        self.customers.append(customer)

    def addMessage(self, message):
        heapq.heappush(self.messages, message)


class Message:
    def __init__(self, content):
        self.content = content
        self.time = datetime.now()
