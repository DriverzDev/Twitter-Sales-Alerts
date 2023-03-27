import DriverzNFT from 0xa039bd7d55a96c0c

pub fun main(accountAddress: Address, nftID: UInt64): DriverzNFT.MetadataViews.Display {
    let account = getAccount(accountAddress)
    let collectionRef = account.getCapability<&DriverzNFT.Collection{DriverzNFT.CollectionPublic}>(DriverzNFT.CollectionPublicPath)
        .borrow()
        ?? panic("Could not borrow DriverzNFT collection reference")

    let nft = collectionRef.borrowNFT(id:nftID)
    let nftDisplay = nft.display()
    
    return nftDisplay
}
