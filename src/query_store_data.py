from src.api import send_post_request_to_api


def get_params_to_query_store_data(cursor, step, include_dlc=False):
    if include_dlc:
        category_str = ""
    else:
        category_str = 'category: "games/edition/base|software/edition/base|editors|bundles/games|freegames/vaulted", '

    query_str = "{Catalog {searchStore"
    query_str += f'({category_str}start: {cursor}, count: {step}, country: "FR") '
    query_str += """{
          elements {
            title
            id
            namespace
            description
            longDescription
            status
            creationDate
            lastModifiedDate
            linkedOfferId
            isFeatured
            ignoreOrder
            freeDays
            technicalDetails
            recurrence
            effectiveDate
            isCodeRedemptionOnly
            keyImages {
              type
              url
            }
            currentPrice
            seller {
              id
              name
            }
            productSlug
            urlSlug
            url
            tags {
              id
            }
            items {
              id
              namespace
            }
            customAttributes {
              key
              value
            }
            categories {
              path
            }
            developerDisplayName
            publisherDisplayName
            prePurchase
            releaseDate
            pcReleaseDate
            viewableDate
            approximateReleasePlan {
              day
              month
              quarter
              year
              releaseDateType
            }
          }
          paging {
            count
            total
          }
        }
      }
    }
    """
    params = {"query": query_str.replace("\n", " ")}

    return params


def to_store_data(cursor, step, include_dlc=False, verbose=True):
    params = get_params_to_query_store_data(cursor, step, include_dlc)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        store_data = data["data"]["Catalog"]["searchStore"]
    except (TypeError, KeyError) as e:
        store_data = None
    return store_data
