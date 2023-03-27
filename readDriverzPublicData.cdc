import DriverzNFT from 0xa039bd7d55a96c0c

pub fun main(userAddress: Address,nftID: UInt64): {String:String} {
    let account = getAccount(userAddress)
    let collectionRef = account.getCapability<&DriverzNFT.Collection{DriverzNFT.CollectionPublic}>(/public/driverzNFTCollection).borrow()
        ?? panic("Could not Borrow collection reference")
    let nftRef = collectionRef.borrowDriverzNFT(id: nftID)
    let template = nftRef.template()

    if template.revealed() {
        return template.metadata!.repr()
    }

    return {
        "NFT ID": nftRef.id.toString(),
        "Set ID": nftRef.setID.toString(),
        "Template ID": nftRef.templateID.toString(),
        "Display Name": template.defaultDisplay.name,
        "Display Description": template.defaultDisplay.description,
        "Display URI": template.defaultDisplay.thumbnail.uri(),
        "Creator": nftRef.creator.toString()
    }
}

 