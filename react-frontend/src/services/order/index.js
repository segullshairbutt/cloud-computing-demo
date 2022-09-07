import Store from '../../redux/store/store'
import { setMyOrders } from '../../redux/slice/order'
import { Request } from '../../constants/api'
import { protectedAxios } from '../instance'

export const getMyOrders = async () => {
    try {
      const res = await protectedAxios.get(Request.GET_MY_ORDERS);
      Store.dispatch(setMyOrders(res.data))
      return res.data
    } catch (err) {
      console.log(JSON.stringify(err))
      throw err
    }
  }