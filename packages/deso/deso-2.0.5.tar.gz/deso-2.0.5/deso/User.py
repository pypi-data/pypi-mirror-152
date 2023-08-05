from urllib import response
import requests


class User:
    def __init__(self,  nodeURL="https://node.deso.org/api/v0/"):
        self.NODE_URL = nodeURL

    def getSingleProfile(self, username="", publicKey="", NoErrorOnMissing=False):
        endpointURL = self.NODE_URL + "get-single-profile"
        payload = {"PublicKeyBase58Check": publicKey,
                   "Username": username, "NoErrorOnMissing": NoErrorOnMissing}
        response = requests.post(endpointURL, json=payload)
        return response

    def getUsersStateless(self, listOfPublicKeys, skipForLeaderboard=True):
        endpointURL = self.NODE_URL + "get-users-stateless"
        payload = {"PublicKeysBase58Check": listOfPublicKeys,
                   "SkipForLeaderboard": skipForLeaderboard}
        response = requests.post(endpointURL, json=payload)
        return response

    def getProfilePicURL(self, publicKey):
        profilePicURL = f'{self.NODE_URL}get-single-profile-picture/{publicKey}?fallback=https://node.deso.org/assets/img/default_profile_pic.png'
        return profilePicURL
    def getMessagesStateless(self, publicKey, numToFetch=25, sortAlgorithm="time", followersOnly=False, followingOnly=False, holdersOnly=False, holdingsOnly=False, fetchAfterPublicKey=""):
        endpointURL = self.NODE_URL + "get-messages-stateless"
        payload = {"PublicKeyBase58Check": publicKey,
                   "FetchAfterPublicKeyBase58Check": fetchAfterPublicKey,
                   "NumToFetch": numToFetch,
                   "HoldersOnly": holdersOnly,
                   "HoldingsOnly": holdingsOnly,
                   "FollowersOnly": followersOnly,
                   "FollowingOnly": followingOnly,
                   "SortAlgorithm": sortAlgorithm}
        response = requests.post(endpointURL, json=payload)
        return response

    def getNotifications(self, publicKey, startIndex=-1, numToFetch=50, filterOutNotificationCategories={}):
        # filterOutNotification is a map that looks like {"diamond": True, "like": True,  "transfer": True, "follow": True, "nft": True, "post": True}
        # ever True means that the specific notification category will be filtered out
        payload = {"PublicKeyBase58Check": publicKey,
                   "FetchStartIndex": startIndex,
                   "NumToFetch": numToFetch,
                   "FilteredOutNotificationCategories": filterOutNotificationCategories}
        endpointURL = "https://diamondapp.com/api/v0/get-notifications"
        response = requests.post(endpointURL, json=payload)
        return response

    def getNFTs(self, userPublicKey, readerPublicKey="", isForSale=False):
        '''Gets the NFTs associated with a user,
            setting isForSale = True returns only the NFTs that are for sale.'''
        payload = {"UserPublicKeyBase58Check": userPublicKey,
                   "ReaderPublicKeyBase58Check": readerPublicKey,
                   "IsForSale": isForSale}

        endpointURL = self.NODE_URL + "get-nfts-for-user"
        response = requests.post(endpointURL, json=payload)
        return response

    def getDerivedKeys(self, publicKey):
        payload = {"PublicKeyBase58Check": publicKey}
        endpointURL = self.NODE_URL + "get-user-derived-keys"
        response = requests.post(endpointURL, json=payload)
        return response

    
    def getTransactionInfo(self, publicKey, limit=200, lastTransactionIDBase58Check="", lastPublicKeyTransactionIndex=-1):
        payload = {"PublicKeyBase58Check": publicKey,
                   "LastTransactionIDBase58Check": lastTransactionIDBase58Check,
                   "LastPublicKeyTransactionIndex": lastPublicKeyTransactionIndex, "Limit": limit}
        endpointURL = self.NODE_URL + "transaction-info"
        response = requests.post(endpointURL, json=payload)
        return response
